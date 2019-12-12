#!/home/opt/intel/intelpython3/bin/python
import pickle
from pprint import pprint


if __name__ == "__main__":
    with open('dirs.pickle', 'rb') as f:
        dirs = pickle.load(f)
    
    print(f'left : {len(dirs)}')    
    for directory in dirs:
        pprint(str(directory))
