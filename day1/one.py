import sys
from os import path


def main(path):
    # make sure the first one will not be greater than it
    tmp = 1000000000000
    with open(path) as opened:
        line = opened.readline()
        greater = 0
        while line:
            if int(line) > int(tmp):
                greater += 1
            tmp = line
            line = opened.readline()
    print("\nAll Done! There were {0} increases!".format(greater))


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
