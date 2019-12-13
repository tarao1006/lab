"""Entory point of simulation.

qsub -N job -o std.out -e std.err -v PICKLE_FILE="dirs.pickle" -v MAX_COUNT=8 -q uni1.q job.sh

Parameters
----------
PICKLE_FILE: str
    Pickle file name to load.
MAX_COUNT: int, default 4[optional]
    Extract count.
CMD: str [optional]
    Command to run.
"""
import os
import sys
import pickle
import subprocess
from pathlib import Path
from copy import deepcopy


class SimulationError(Exception):
    pass


class FileNotSelectedError(SimulationError):
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
    pickle_file = os.getenv('PICKLE_FILE')
    cmd = os.getenv('CMD')
    max_count = os.getenv('MAX_COUNT')

    if pickle_file is None:
        raise FileNotSelectedError("Pickle file is not selected.")

    if cmd is None:
        cmd = '~/bin/kapsel -Iinput.udf -Ooutput.udf -Ddefine.udf -Rrestart.udf'

    if max_count is None:
        max_count = 4
    else:
        max_count = int(max_count)

    pickle_filepath = Path(pickle_file)
    sim_dirs = extracet_list(pickle_filepath, max_count=max_count)
    if sim_dirs is None:
        print(f"End of sim", file=sys.stdout)
    else:
        for sim_dir in sim_dirs:
            cwd = str(sim_dir)
            with (sim_dir / 'output.txt').open(mode='wb') as f:
                for line in get_lines(cmd=cmd, cwd=cwd):
                    f.write(line)
