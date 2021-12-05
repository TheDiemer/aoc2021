class Board:
    """A structure of a 5x5 board with individual spots having the Number And a drawn value."""

    def __init__(self, row1, row2, row3, row4, row5):
        """Creates the individual slots and rows/columns."""
        self.one = [row1[0], None]
        self.two = [row1[1], None]
        self.three = [row1[2], None]
        self.four = [row1[3], None]
        self.five = [row1[4], None]
        self.six = [row2[0], None]
        self.seven = [row2[1], None]
        self.eight = [row2[2], None]
        self.nine = [row2[3], None]
        self.ten = [row2[4], None]
        self.eleven = [row3[0], None]
        self.twelve = [row3[1], None]
        self.thirteen = [row3[2], None]
        self.fourteen = [row3[3], None]
        self.fifteen = [row3[4], None]
        self.sixteen = [row4[0], None]
        self.seventeen = [row4[1], None]
        self.eighteen = [row4[2], None]
        self.nineteen = [row4[3], None]
        self.twenty = [row4[4], None]
        self.twentyone = [row5[0], None]
        self.twentytwo = [row5[1], None]
        self.twentythree = [row5[2], None]
        self.twentyfour = [row5[3], None]
        self.twentyfive = [row5[4], None]
        self.row1 = [self.one, self.two, self.three, self.four, self.five]
        self.row2 = [self.six, self.seven, self.eight, self.nine, self.ten]
        self.row3 = [
            self.eleven,
            self.twelve,
            self.thirteen,
            self.fourteen,
            self.fifteen,
        ]
        self.row4 = [
            self.sixteen,
            self.seventeen,
            self.eighteen,
            self.nineteen,
            self.twenty,
        ]
        self.row5 = [
            self.twentyone,
            self.twentytwo,
            self.twentythree,
            self.twentyfour,
            self.twentyfive,
        ]
        self.col1 = [
            self.row1[0],
            self.row2[0],
            self.row3[0],
            self.row4[0],
            self.row5[0],
        ]
        self.col2 = [
            self.row1[1],
            self.row2[1],
            self.row3[1],
            self.row4[1],
            self.row5[1],
        ]
        self.col3 = [
            self.row1[2],
            self.row2[2],
            self.row3[2],
            self.row4[2],
            self.row5[2],
        ]
        self.col4 = [
            self.row1[3],
            self.row2[3],
            self.row3[3],
            self.row4[3],
            self.row5[3],
        ]
        self.col5 = [
            self.row1[4],
            self.row2[4],
            self.row3[4],
            self.row4[4],
            self.row5[4],
        ]

    def check(self):
        """Checks columns and rows to see if this board has won."""
        for column in [self.col1, self.col2, self.col3, self.col4, self.col5]:
            tmp = 0
            for item in column:
                if item[1] is not None:
                    tmp += 1
            if tmp == 5:
                return True

        for row in [self.row1, self.row2, self.row3, self.row4, self.row5]:
            tmp = 0
            for item in row:
                if item[1] is not None:
                    tmp += 1
            if tmp == 5:
                return True

        return False

    def drawn(self, number, position):
        """Checks if the number drawn is on this board.
        If it is, store that position and return True.
        Otherwise, store nothing and return False."""
        drawn = False
        for row in [self.row1, self.row2, self.row3, self.row4, self.row5]:
            for item in row:
                if item[0] == number:
                    item[1] = position
                    drawn = True
        return drawn

    def unmarkedSum(self):
        """Provides the sum of all the numbers that were unmarked."""
        unmarked = []
        for column in [self.col1, self.col2, self.col3, self.col4, self.col5]:
            for item in column:
                if item[1] is None:
                    unmarked.append(int(item[0]))
        return sum(unmarked)

    def winningPosition(self, position):
        self.wp = position

    def pprint(self):
        """Nicely print a bingo board."""
        print("---------BINGOOOO--------")
        for row in [self.row1, self.row2, self.row3, self.row4, self.row5]:
            string = ""
            for item in row:
                if item[1] is None:
                    string += f"| {item[0]} "
                else:
                    string += f"|*{item[0]} "
            string += "|"
            print(string)
            print("-------------------------")
