import sys
from os import path


class Fish:
    """A class to track the fish."""
    
    def __init__(self, age):
        if age is None:
            self.timer = 8
        else:
            self.timer = age

    def count(self):
        age = self.timer
        if age == 0:
            self.timer = 6
            return Fish(None)
        else:
            self.timer = age - 1
            return None

def parse(path):
    with open(path) as opened:
        content = opened.read().strip().split(",")
    return content


def main(path):
    ages = parse(path)
    fish = []
    for age in ages:
        fish.append(Fish(int(age)))

    for one in fish:
        print(f"I'm a new fish at age: {one.timer}")

    for day in range(0,80):
        print(f"dawn of day {day}")
        tmpFish = fish.copy()
        # On each day I need to count Each fish
        for one in fish:
            tmp = one.count()
            if tmp is not None:
                tmpFish.append(tmp)
        fish = tmpFish.copy()
    print(len(fish))

    #numbers, boards = parse(path)
    #for a in boards:
    #    a.pprint()

    #i = 0
    #win = False
    #winner = None
    #for number in numbers:
    #    for board in boards:
    #        wasDrawn = board.drawn(number, i)
    #        win = board.check()
    #        if win:
    #            winner = board
    #            break
    #    if win:
    #        break
    #    i += 1
    #print(
    #    "\nAnd, with the {0}th ball drawn ({1}), This is the winning Board!".format(
    #        i + 1, numbers[i]
    #    )
    #)
    #winner.pprint()
    #final = winner.unmarkedSum() * int(numbers[i])
    #print(
    #    "which means the final score with this board would be: {0} * {1} = {2}".format(
    #        winner.unmarkedSum(), numbers[i], final
    #    )
    #)


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
