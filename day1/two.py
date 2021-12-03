import sys
from os import path


def add(depth, place, line):
    if depth.get(place, "") == "":
        depth[place] = [int(line)]
    else:
        tmp = depth[place]
        tmp.append(int(line))
        depth[place] = tmp


def main(path):
    depth = []
    with open(path) as opened:
        line = opened.readline()
        while line:
            depth.append(int(line))
            line = opened.readline()

    tmp = 0
    numbers = []
    while tmp < len(depth):
        if (len(depth) - 1) - tmp <=2:
            try:
                numbers.append(depth[tmp] + depth[tmp+1])
            except:
                numbers.append(depth[tmp])
        else:
            numbers.append(depth[tmp] + depth[tmp+1] + depth[tmp+2])
        tmp += 1
    tmp = 1
    greater = 0
    while tmp < len(numbers):
        if numbers[tmp] > numbers[tmp-1]:
            greater += 1
        tmp +=1
    print(greater)

#    tmp = 10000000000000
#    greater = 0
#    for place in list(depth.keys()):
#        row = depth[place][0] + depth[place][1] + depth[place][2]
#        print("is row: {0} > tmp: {1}?".format(row, tmp))
#        if row > tmp:
#            greater += 1
#            print("yes, {0}".format(greater))
#        tmp = row
#    print(greater)


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
