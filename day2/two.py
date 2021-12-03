import sys
from os import path


def main(path):
    horiz = 0
    depth = 0
    aim = 0
    with open(path) as opened:
        line = opened.readline()
        while line:
            if "forward" in line:
                tmp = int(line.split(" ")[1])
                horiz += tmp
                depth += aim*tmp
            if "down" in line:
                aim += int(line.split(" ")[1])
            if "up" in line:
                aim -= int(line.split(" ")[1])
            line = opened.readline()
    print("{0} * {1} = {2}".format(horiz, depth, horiz*depth))


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
