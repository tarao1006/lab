"""
指定したディレクトリを探索し、input.udfとdefine.udfが存在した場合、
そのディレクトリを保存する。全て探索したのちに、保存したディレクトリに
移動しながらkapselを実行する。

qsub -N job -o std.out -e std.err -v SIM_NUM=0 -v MAX_COUNT=8 -v IS_FIRST=1 -q uni1.q job.sh
"""
import os
import sys
import glob
import pickle
import subprocess
from pathlib import Path
from collections.abc import Sequence
from functools import partial
from copy import deepcopy


class SumulationNotSelectedError(Exception):
    pass


def get_lines(cmd, cwd):
    """Run command in sub process and yeild stdout/stderr.

    Parameters
    ----------
    cmd: str
        Command executed

    Yeilds
    ------
    bytes
        stdout/stderr string
    """
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break


def scan_dir(contents, path_dir=None) -> list:
    """Look for dirs which have contents.

    Parameters
    ----------
    contents: str or list of str
        File list to look for. This must have more than 2.
    path_dir: str or None

    Returns
    -------
    list of Path
        Directories which have both of input.udf and defin.udf.
        If path_dir is invalid or there is no directories which
        have both of input.udf and defin.udf, return None.
    """
    if not isinstance(contents, Sequence):
        raise TypeError(f"contents have to be sequence type, but '{contents}' is {type(contents)}")
    if len(contents) < 2:
        raise TypeError(f"contents have to be more than 2 elements, "
                        f"but {contents} have {len(contents)} elemtent.")

    if path_dir is None:
        path_dir = '.'
    if not isinstance(path_dir, str):
        raise TypeError(f"'{path_dir}' is not str. path_dir must be str.")

    if path_dir == '.':
        path_dir = Path.cwd()
    elif path_dir.startswith('./'):
        path_dir = Path.cwd() / str(path_dir)[2:]

    path_dir = Path(path_dir)

    file_sets = []
    for content in contents:
        file_sets.append(set(Path(filename).parent for filename in glob.glob(f'{str(path_dir)}/**/{content}', recursive=True)))

    dirs = file_sets[0] & file_sets[1]
    if len(file_sets) >= 3:
        for file_set in file_sets[2:]:
            dirs = dirs & file_set

    if dirs == set():
        return []

    dirs = list(dirs)
    dirs.sort()

    return dirs


scan_kapsel_simulation_dirs = partial(scan_dir, contents=['input.udf', 'define.udf'])


def extracet_list(filename, path_dir=None, max_count=1) -> list:
    """Extract some elements from pickled list.

    Parameters
    ----------
    filename: str or Path
        Pickle file to load.
    path_dir: str, Path or None
    max_count: int
        Maximun count of extraction.

    Returns
    -------
    list of str:
        Extracted list.

    Raises
    ------
    FileNotFoundError:
        If file does not exist.
    """
    if isinstance(filename, str):
        filename = Path(filename)
    if not isinstance(filename, Path):
        raise TypeError(f"filename must be str or pathlib.Path")

    if path_dir is None:
        path_dir = Path('.')
    if not (isinstance(path_dir, str) or isinstance(path_dir, Path)):
        raise TypeError(f"path_dir must be str.")

    path_dir = Path(path_dir)

    if not isinstance(max_count, int):
        raise TypeError(f"max_count must be int")

    full_filename = path_dir / filename
    with full_filename.open(mode='rb') as f:
        dirs = pickle.load(f)

    if len(dirs) == 0:
        return
    if len(dirs) <= max_count:
        max_count = len(dirs)

    extracted_list = deepcopy(dirs[:max_count])

    remain_list = dirs[max_count:]
    with full_filename.open(mode='wb') as f:
        pickle.dump(remain_list, f)

    return extracted_list


if __name__ == "__main__":
    is_first = os.getenv('IS_FIRST')
    sim_num = os.getenv('SIM_NUM')
    max_count = os.getenv('MAX_COUNT')

    if is_first is None:
        is_first = False
    else:
        is_first = True

    if sim_num is None:
        raise SumulationNotSelectedError(
            "select simulation nuber using command line argument like '-v SIM_NUM=0'"
        )
        sys.exit(1)
    else:
        sim_num = int(sim_num)
    sim_num_str = f'{sim_num:0=2}'

    if max_count is None:
        max_count = 4
    else:
        max_count = int(max_count)

    if is_first:
        simulation_dirs = scan_kapsel_simulation_dirs(path_dir=f'./sim{sim_num_str}')
        if len(simulation_dirs) >= 0:
            with open('dirs.pickle', 'wb') as f:
                pickle.dump(simulation_dirs, f)

    cmd = '~/bin/kapsel -Iinput.udf -Ooutput.udf -Ddefine.udf -Rrestart.udf'

    dirs_pickle = Path('dirs.pickle')
    sim_dirs = extracet_list(dirs_pickle, max_count=max_count)
    if sim_dirs is None:
        print(f"End of 'sim{sim_num}'", file=sys.stdout)
        print(f"Delete {dirs_pickle}...", file=sys.stdout)
        dirs_pickle.unlink()
        print("Done", file=sys.stdout)
    else:
        print(sim_dirs)
        for sim_dir in sim_dirs:
            cwd = str(sim_dir)
            with (sim_dir / 'output.txt').open(mode='wb') as f:
                for line in get_lines(cmd=cmd, cwd=cwd):
                    f.write(line)
