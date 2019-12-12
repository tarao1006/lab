"""
指定したディレクトリを探索し、input.udfとdefine.udfが存在した場合、
そのディレクトリを保存する。全て探索したのちに、保存したディレクトリに
移動しながらkapselを実行する。
"""
import glob
import subprocess
from pathlib import Path


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


def scan_simulation_dir(path_dir=None) -> list:
    """

    Parameters
    ----------
    path_dir: str, Path or None

    Returns
    -------
    sequence of Path or None
        Directories which have both of input.udf and defin.udf.
        If path_dir is invalid or there is no directories which
        have both of input.udf and defin.udf, return None.
    """
    if path_dir is None:
        path_dir = Path('.')
    if not (isinstance(path_dir, str) or isinstance(path_dir, Path)):
        raise TypeError(f"'{path_dir}' is not str. path_dir must be str.")

    path_dir = Path(path_dir)

    input_parents = set(Path(filename).parent for filename in glob.glob(f'{str(path_dir)}/**/input.udf', recursive=True))
    define_parents = set(Path(filename).parent for filename in glob.glob(f'{str(path_dir)}/**/define.udf', recursive=True))

    simulation_dirs = input_parents & define_parents
    if simulation_dirs == set():
        return None

    return simulation_dirs
