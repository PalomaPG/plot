# -*- encoding: utf-8 -*-

from Performance import Performance
import sys

def main(path, prefix):

    p = Performance(path, prefix)
    p.writeAllFiles()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])