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


def main(path):
    bits = parse(path)
    gamma = []
    epsilon = []
    value = {}
    for i in range(0, len(bits)):
        for j in range(0, len(bits[0])):
            if value.get(j, None) is None:
                value[j] = int(bits[i][j])
            else:
                tmp = int(value[j])
                tmp += int(bits[i][j])
                value[j] = tmp
    length = len(bits)
    for key in value:
        if value[key] >= (length)/2:
            gamma.append("1")
            epsilon.append("0")
        else:
            epsilon.append("1")
            gamma.append("0")
    gam_ans = binToDec("".join(gamma))
    eps_ans = binToDec("".join(epsilon))
    power = gam_ans * eps_ans
    print("power consumption: {0}".format(power))



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
