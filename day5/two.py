import sys
from os import path
import re
from collections import defaultdict


def main(path):
    vents = parse(path)
    grid = defaultdict(int)
    diagonals = []

    for line in vents:
        x1, y1, x2, y2 = line
        # horizontal
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                grid[(i, y1)] += 1
        # vertical
        elif x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                grid[(x1, i)] += 1
        else:
            diagonals.append(line)
    for line in diagonals:
        x1, y1, x2, y2 = line
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        for i in range(abs(x2-x1)+1):
            grid[(x1+i*dx, y1+i*dy)] += 1

    part2 = sum([1 if v > 1 else 0 for v in grid.values()])
    print(grid)
    print(part2)


def parse(path):
    vents = []
    with open(path) as opened:
        line = opened.readline()
        while line:
            vents.append(list(map(int, re.findall("\d+", line))))
            line = opened.readline()
    return vents


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filePath = sys.argv[1]
        if not path.isfile(path.expanduser(filePath)):
            print(
                "This ({0}) is not a valid file Path! Please put the input file in place and try again!".format(
                    filePath
                )
            )
        else:
            main(path.expanduser(filePath))
    else:
        print("Nope, just provide a file path")
