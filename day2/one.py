import sys
from os import path


def main(path):
    x = 0
    y = 0
    with open(path) as opened:
        line = opened.readline()
        while line:
            if "forward" in line:
                x += int(line.split(" ")[1])
            if "down" in line:
                y += int(line.split(" ")[1])
            if "up" in line:
                y -= int(line.split(" ")[1])
            line = opened.readline()
    print("{0} * {1} = {2}".format(x, y, x*y))


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
