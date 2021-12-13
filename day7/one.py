import math
from os import path
import sys



def parse(path):
    crabs = {}
    with open(path) as opened:
        content = list(map(int,opened.read().strip().split(",")))
    return content


def main(path):
    crabs = parse(path)
    print(crabs)
    left = min(crabs)
    right = max(crabs)
    position = left
    tmp_sort = sorted(crabs)
    print(f"{tmp_sort} is this long: {len(tmp_sort)}")
    if len(tmp_sort) % 2 == 0:
        # Even
        tmp = int(len(tmp_sort)/2)
        tmp2 = tmp+1
        med = int((tmp_sort[tmp] + tmp_sort[tmp2]) / 2)
        if med not in tmp_sort:
            med = tmp_sort[med]
    else:
        # Odd
        med = tmp_sort[int(math.ceil(len(tmp_sort)/2))]

    print(med)
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - med)
    print(fuel)


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
