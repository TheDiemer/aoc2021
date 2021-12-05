import sys
from os import path
from board import Board


def parse(path):
    with open(path) as opened:
        line = opened.readline().strip()
        pos = 0
        boardsV1 = []
        while line:
            if pos == 0:
                numbers = line.split(",")
                pos += 1
                line = opened.readline()
            else:
                boardsV1.append(line)
                line = opened.readline()

    boards = []
    pos = 1
    while pos < len(boardsV1):
        row1 = boardsV1[pos].strip().split()
        row2 = boardsV1[pos + 1].strip().split()
        row3 = boardsV1[pos + 2].strip().split()
        row4 = boardsV1[pos + 3].strip().split()
        row5 = boardsV1[pos + 4].strip().split()
        boards.append(Board(row1, row2, row3, row4, row5))
        pos += 6

    return numbers, boards


def main(path):
    numbers, boards = parse(path)
    for a in boards:
        a.pprint()

    i = 0
    place = 1
    loser = None
    for number in numbers:
        for board in boards:
            win = False
            wasDrawn = board.drawn(number, i)
            win = board.check()
            if win:
                try:
                    check = board.wp
                except AttributeError:
                    board.winningPosition(place)
                    place += 1
                if place > len(boards):
                    loser = board
                    break
        if loser is not None:
            break
        i += 1

    print(
        "\nAnd, with the {0}th ball drawn ({1}), This is the worst Board!".format(
            i + 1, numbers[i]
        )
    )
    loser.pprint()
    final = loser.unmarkedSum() * int(numbers[i])
    print(
        "which means the final score with this board would be: {0} * {1} = {2}".format(
            loser.unmarkedSum(), numbers[i], final
        )
    )


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
