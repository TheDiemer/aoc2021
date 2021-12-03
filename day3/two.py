import sys
from os import path


def parse(path):
    bits = []
    with open(path) as opened:
        line = opened.readline()
        while line:
            bits.append(line.strip())
            line = opened.readline()
    return bits


def binToDec(binary):
    return int(binary,2)

def mostLeastCommon(array):
    value = {}
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if value.get(j, None) is None:
                value[j] = int(array[i][j])
            else:
                tmp = int(value[j])
                tmp += int(array[i][j])
                value[j] = tmp
    return value

def thing(bits, most):
    value = mostLeastCommon(bits)
    newbits = bits
    place = 0
    while True:
        tmp = []
        length = len(newbits)
        for row in newbits:
            if most:
                if value[place] >= length/2:
                    if row[place] == "1":
                        tmp.append(row)
                else:
                    if row[place] == "0":
                        tmp.append(row)
            else:
                if value[place] >= length/2:
                    if row[place] == "0":
                        tmp.append(row)
                else:
                    if row[place] == "1":
                        tmp.append(row)

        value = mostLeastCommon(tmp)
        newbits = tmp
        place += 1
        if len(newbits) <= 1:
            break
    return newbits

def main(path):
    bits = parse(path)
    oxygen = thing(bits, True)
    co2 = thing(bits, False)
    oxy_ans = binToDec(str(oxygen[0]))
    co2_ans = binToDec(str(co2[0]))
    print("life support: {0}".format(oxy_ans * co2_ans))


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
