import sys

import os


if __name__ == "__main__":
    a = 100
    b = sys.getsizeof(a)

    c = os.getenv('HOME')
    print(c)
