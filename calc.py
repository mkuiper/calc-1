"""calc.py: A simple calculator."""

import sys

if __name__ == '__main__':
    print(sum(map(float, sys.argv[1:])))
