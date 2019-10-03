import sys

import src.loader as loader

def launch():
    loader.load(sys.argv[1:] if sys.argv[1:] else [])

if __name__ == "__main__":
    launch()