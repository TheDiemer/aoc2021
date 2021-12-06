import sys
from os import path

def count_lanternfish(fish, days):
    # We will count how many fish are at each of the possible timer positions:
    # 0 - 8, which is 9 positions, so make an array 9 positions long full of 0
    cycle_counts = [0] * 9
    # now lets loop over our starting fish
    for cycle in fish:
        # and for every timer count the fish start with, add a new count to 
        # that position
        # for example: if fish is [1, 2, 3], the cycle_counts array would
        # end up starting like: [0, 1, 1, 1, 0, 0, 0, 0, 0]
        cycle_counts[cycle] += 1

    # Now lets loop for the number of days we want to check, but we don't care
    # about that value, so drop it into _
    for _ in range(days):
        # rotate the values and add in the number of new fish that need to be
        # added before setting the cycle back as the value before looping again
        new_cycle_counts = cycle_counts[1:] + cycle_counts[:1]
        new_cycle_counts[6] += cycle_counts[0]
        cycle_counts = new_cycle_counts
    # And since we counted the number of fish at each position, we simply need
    # to add up all those values
    return sum(cycle_counts)


def main(path):
    starting_fish = open(path).read().split(",")
    lanternfish = list(map(int, starting_fish))
    part1 = count_lanternfish(lanternfish, 80)
    part2 = count_lanternfish(lanternfish, 256)
    print(f"Part1: {part1}, Part2: {part2}")


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
