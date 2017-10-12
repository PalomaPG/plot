# -*- encoding: utf-8 -*-
from Plot import Plot
import sys

def main(path1, path2, title, xlabel, ylabel):
    p = Plot(path1, path2, title, xlabel, ylabel)
    p.plot()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
