"""Entory point of simulation.

qsub -N job -o std.out -e std.err -v SIM_NUM=0 -v MAX_COUNT=8 -v IS_FIRST=1 -q uni1.q job.sh

Parameters
----------
SIM_NUM: int (0~999)
    Main simulation number.
SUB_SIM_NUM: int (0~999) [optional]
    Sub simulation number.
MAX_COUNT: int, default 4[optional]
    Extract count.
IS_FIRST: bool (0 or 1) [optional]
    If do this simulation at first.
DONOT_DO: bool (0 or 1) [optional]
    If do simulation or not.
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


class SimulationError(Exception):
    pass


class SumulationNotSelectedError(SimulationError):
    pass


def get_lines(cmd, cwd):
    """Run command in sub process and yeild stdout/stderr.

    Parameters
    ----------
    cmd: str
        Command executed.

    Yeilds
    ------
    bytes
        String of stdout/stderr.
    """
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break


def scan_dir(filenames, path_dir=None) -> list:
    """Look for dirs that contain filenames.

    Parameters
    ----------
    filenames: sequence of str
        File list to look for. This must have more than 2.
    path_dir: str or None
        Path to look for the filenames in. If None, filenames
        need to be absolute or be in the cwd.

    Returns
    -------
    dirs: list of pathlib.Path
        Directories which have both of input.udf and defin.udf.
        If path_dir is invalid or there is no directories which
        have both of input.udf and defin.udf, return None.

    Raises
    ------
    FileNotFoundError:
        If threre is no directory that contain all of filenames elements.
    """
    if not isinstance(filenames, Sequence):
        raise TypeError(f"filenames have to be sequence.")
    if len(filenames) < 2:
        raise TypeError(f"filenames need to have more than 2 elements.")

    if path_dir is None:
        path_dir = '.'
    if not isinstance(path_dir, str):
        raise TypeError(f"path_dir must be str.")

    if path_dir == '.':
        path_dir = Path.cwd()
    elif path_dir.startswith('./'):
        path_dir = Path.cwd() / str(path_dir)[2:]

    path_dir = Path(path_dir)

    file_sets = []
    for searchfilename in filenames:
        file_sets.append(set(Path(filename).parent for filename in glob.glob(f'{str(path_dir)}/**/{searchfilename}', recursive=True)))

    dirs = file_sets[0] & file_sets[1]
    if len(file_sets) >= 3:
        for file_set in file_sets[2:]:
            dirs = dirs & file_set

    if dirs == set():
        raise FileNotFoundError(f"Threre is no directory that contain all of {filenames}")

    dirs = list(dirs)
    dirs.sort()

    return dirs


scan_kapsel_simulation_dirs = partial(scan_dir, contents=['input.udf', 'define.udf'])


def extracet_list(pickled_filename, path_dir=None, max_count=1, with_delete=False) -> list:
    """Extract some elements from pickled list.

    Parameters
    ----------
    pickled_filename: str or pathlib.Path
        Pickle file to load.
    path_dir: str, Path or None
        Path to look for the pickled_filename in. If None,
        pickled_filename need to be absolute or be in the cwd.
    max_count: int
        Maximun count to extract.
    with_delete: bool
        If delete pickle when remain_dirs is empty.

    Returns
    -------
    list of pathlib.Path:
        Extracted list.

    Raises
    ------
    TypeError
    FileNotFoundError:
        If file does not exist.
    """
    if isinstance(pickled_filename, str):
        pickled_filename = Path(pickled_filename)
    if not isinstance(pickled_filename, Path):
        raise TypeError(f"filename must be str or pathlib.Path")

    if path_dir is None:
        path_dir = Path('.')
    if isinstance(path_dir, str):
        path_dir = Path(path_dir)
    if not isinstance(path_dir, Path):
        raise TypeError(f"path_dir must be str or Path.")

    if not isinstance(max_count, int):
        raise TypeError(f"max_count must be int")

    full_filename = path_dir / pickled_filename
    if not full_filename.exists():
        raise FileNotFoundError(f"{full_filename} does not exist.")

    with full_filename.open(mode='rb') as f:
        dirs = pickle.load(f)

    if len(dirs) == 0 and with_delete:
        full_filename.unlink()
        return
    if len(dirs) <= max_count:
        max_count = len(dirs)

    extracted_list = deepcopy(dirs[:max_count])

    remain_list = dirs[max_count:]
    if len(remain_list) == 0 and with_delete:
        full_filename.unlink()
    else:
        with full_filename.open(mode='wb') as f:
            pickle.dump(remain_list, f)

    return extracted_list


if __name__ == "__main__":
    is_first = os.getenv('IS_FIRST')
    donot_do = os.getenv('DONOT_DO')
    sim_num = os.getenv('SIM_NUM')
    sub_sim_num = os.getenv('SUB_SIM_NUM')
    max_count = os.getenv('MAX_COUNT')

    if is_first is None:
        is_first = False
    else:
        is_first = True

    if donot_do is None:
        is_first = False
    else:
        donot_do = True

    if sim_num is None:
        raise SumulationNotSelectedError(
            "select simulation nuber using command line argument like '-v SIM_NUM=0'"
        )
        sys.exit(1)
    else:
        sim_num = int(sim_num)
    sim_num_str = f'{sim_num:0=3}'

    if sub_sim_num is not None:
        sub_sim_num = int(sub_sim_num)
        sub_sim_num_str = f'{sub_sim_num:0=3}'

        sim_num_str += f'-{sub_sim_num_str}'

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

    if not donot_do:
        dirs_pickle = Path('dirs.pickle')
        sim_dirs = extracet_list(dirs_pickle, max_count=max_count)
        cmd = 'll'
        for sim_dir in sim_dirs:
            cwd = str(sim_dir)
            with (sim_dir / 'output.txt').open(mode='wb') as f:
                for line in get_lines(cmd=cmd, cwd=cwd):
                    f.write(line)
        # dirs_pickle = Path('dirs.pickle')
        # sim_dirs = extracet_list(dirs_pickle, max_count=max_count)
        # if sim_dirs is None:
        #     print(f"End of 'sim{sim_num}'", file=sys.stdout)
        # else:
        #     for sim_dir in sim_dirs:
        #         cwd = str(sim_dir)
        #         with (sim_dir / 'output.txt').open(mode='wb') as f:
        #             for line in get_lines(cmd=cmd, cwd=cwd):
        #                 f.write(line)
