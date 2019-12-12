"""
指定したディレクトリを探索し、input.udfとdefine.udfが存在した場合、
そのディレクトリを保存する。全て探索したのちに、保存したディレクトリに
移動しながらkapselを実行する。
"""
import glob
import pickle
import subprocess
from pathlib import Path
from collections.abc import Sequence
from functools import partial


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
    """

    Parameters
    ----------
    contents: str or list of str
        File list to look for. This must have more than 2.
    path_dir: str, Path or None

    Returns
    -------
    sequence of Path or None
        Directories which have both of input.udf and defin.udf.
        If path_dir is invalid or there is no directories which
        have both of input.udf and defin.udf, return None.
    """
    if not isinstance(contents, Sequence):
        raise TypeError(f"contents have to be sequence type, but '{contents}' is {type(contents)}")
    if len(contents) < 2:
        raise TypeError(f"contents have to more than 2 elements, "
                        f"but {contents} have {len(contents)} elemtent.")

    if path_dir is None:
        path_dir = Path('.')
    if not (isinstance(path_dir, str) or isinstance(path_dir, Path)):
        raise TypeError(f"'{path_dir}' is not str. path_dir must be str.")

    path_dir = Path(path_dir)

    file_sets = []
    for content in contents:
        file_sets.append(set(Path(filename).parent for filename in glob.glob(f'{str(path_dir)}/**/{content}', recursive=True)))

    dirs = file_sets[0] & file_sets[1]
    if len(file_sets) >= 3:
        for file_set in file_sets[2:]:
            dirs = dirs & file_set

    if dirs == set():
        return None

    return dirs


scan_kapsel_simulation_dirs = partial(scan_dir, contents=['input.udf', 'define.udf'])


if __name__ == "__main__":
    simulation_dirs = scan_kapsel_simulation_dirs(path_dir='.')
    with open('dirs.pickle', 'wb') as f:
        pickle.dump(simulation_dirs, f)
    with open('dirs.pickle', 'rb') as f:
        dirs = pickle.load(f)

    print(dirs)
