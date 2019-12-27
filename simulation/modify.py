import pickle
import argparse
from pathlib import Path
from pprint import pprint


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="pickle file name", type=str, default="dirs.pickle")
    args = parser.parse_args()
    pickle_filename = Path(args.filename)

    with pickle_filename.open(mode='rb') as f:
        dirs = pickle.load(f)

    new_dirs = []
    left = list(map(int, input('input left index:\n').split(' ')))
    for i, direc in enumerate(dirs):
        if i in left:
            new_dirs.append(direc)

    with pickle_filename.open(mode='wb') as f:
        pickle.dump(new_dirs, f)

