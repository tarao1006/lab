""" Create pickled list of simulation dirs.

"""
import glob
import pickle
import argparse
from pathlib import Path
from collections.abc import Sequence
from functools import partial


class SimulationError(Exception):
    pass


class SumulationNotSelectedError(SimulationError):
    pass


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


scan_kapsel_simulation_dirs = partial(scan_dir, filenames=['input.udf', 'define.udf'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help='simulation number', type=int)
    parser.add_argument("-f", "--filename", help="pickle file name", type=str, default="dirs.pickle")
    parser.add_argument("-ss", "--sub-sim-num", help="sub simlation number", type=int)
    args = parser.parse_args()

    sim_num = args.num
    sim_num_str = f'{sim_num:0=2}'
    sub_sim_num = args.sub_sim_num
    pickle_filename = args.filename

    if sub_sim_num is not None:
        sub_sim_num_str = f'{sub_sim_num:0=2}'

    if sub_sim_num_str:
        simulation_dirs = scan_kapsel_simulation_dirs(path_dir=f'./sim{sim_num_str}/sim{sim_num_str}-{sub_sim_num_str}')
    else:
        simulation_dirs = scan_kapsel_simulation_dirs(path_dir=f'./sim{sim_num_str}')
    with Path(pickle_filename).open(mode='wb') as f:
        pickle.dump(simulation_dirs, f)
