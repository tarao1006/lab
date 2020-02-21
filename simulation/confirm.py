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

    left_num = len(dirs)
    print(f'left : {left_num}')
    for directory in dirs:
        pprint(str(directory))

    if left_num == 0:
        print(f"Remove {pickle_filename}? (y/n)")
        reply = input()
        if reply.upper() == 'Y' or reply.upper() == 'YES':
            pickle_filename.unlink()
