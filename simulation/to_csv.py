"""
Put this file in the directory which output.txt files are saved in.
This file will run after kapsel calcuration ended.
"""
import sys
import glob
import argparse
from pathlib import Path

sys.path.append(f'/Users/taiga/Projects/lab/simulation/utils')
from compress import create_csv, gather_csv


def create_gather_data(path_dir=None):
    """
    """
    if path_dir is None:
        path_dir = '.'
    if not isinstance(path_dir, str):
        raise TypeError(f"path_dir must be str.")

    if path_dir == '.':
        path_dir = Path.cwd()
    elif path_dir.startswith('./'):
        path_dir = Path.cwd() / str(path_dir)[2:]

    path_dir = Path(path_dir)

    text_files = [Path(filename) for filename in glob.glob(f'{path_dir}/**/output.txt', recursive=True)]

    for text_file in text_files:
        create_csv(text_file)

    csv_files = [Path(filename) for filename in glob.glob(f'{path_dir}/**/output.csv', recursive=True)]
    csv_files.sort()

    gather_csv(csv_files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help='simulation number', type=int)
    parser.add_argument("-ss", "--sub-sim-num", help="sub simlation number", type=int)
    args = parser.parse_args()

    sim_num = args.num
    sim_num_str = f'{sim_num:0=2}'
    sub_sim_num = args.sub_sim_num

    if sub_sim_num is not None:
        sub_sim_num_str = f'{sub_sim_num:0=2}'

    if sub_sim_num:
        path_dir = f'./sim{sim_num_str}/sim{sim_num_str}-{sub_sim_num_str}'
    else:
        path_dir = f'./sim{sim_num_str}'

    create_gather_data(path_dir=path_dir)
