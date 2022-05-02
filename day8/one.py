import sys
from os import path


def parse(path):
    input = []
    with open(path) as opened:
        line = opened.readline()
        while line:
            part1, part2 = line.split(" | ")
            input.append({"signal": part1, "output": part2})
            line = opened.readline()
    return input

digits = {
        0: {"letters": ["a", "b", "c", "e", "f", "g"],}, # 6
        1: {"letters": ["c", "f"],}, # 2
        2: {"letters": ["a", "c", "d", "e", "g"],}, # 5
        3: {"letters": ["a", "c", "d", "f", "g"],}, # 5
        4: {"letters": ["b", "c", "d", "f"],}, # 4
        5: {"letters": ["a", "b", "d", "f", "g"],}, # 5
        6: {"letters": ["a", "b", "d", "e", "f", "g"],}, # 6
        7: {"letters": ["a", "c", "f"],}, # 3
        8: {"letters": ["a", "b", "c", "d", "e", "f", "g"],}, # 7
        9: {"letters": ["a", "b", "c", "d", "f", "g"],}, # 6
}

def main(path):
    data = parse(path)
    output = 0
    for row in data:
        for numb in row["output"].split():
            if numb.strip() != "":
                print(f"Checking the length ({len(numb)}) of {numb} to see if it Could be 1 (2), 4 (4), 7 (3), or 8 (7)", end="")
                if len(numb) == len(digits[1]["letters"]):
                    output += 1
                    print("*", end="")
                if len(numb) == len(digits[4]["letters"]):
                    output += 1
                    print("*", end="")
                if len(numb) == len(digits[7]["letters"]):
                    output += 1
                    print("*", end="")
                if len(numb) == len(digits[8]["letters"]):
                    output += 1
                    print("*", end="")
                print("")
    print(output)


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
