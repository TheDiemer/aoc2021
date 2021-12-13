import math
from os import path
import sys



def parse(path):
    crabs = {}
    with open(path) as opened:
        content = list(map(int,opened.read().strip().split(",")))
    return content


def main(path):
    #crabs = parse(path)
    data = parse(path)
    #print(crabs)
    #left = min(crabs)
    #right = max(crabs)
    #position = left
    #tmp_sort = sorted(crabs)
    tmp=[sum(map(lambda x: abs(x-z), data)) for z in range(min(data), max(data)+1)]
    print(tmp)
    tmp2= [sum(map(lambda x: abs(abs(x-z) * (1 + abs(x-z)) / 2), data)) for z in range(min(data), max(data)+1)]
    print(tmp2)
    print ("Part 1:", min([sum(map(lambda x: abs(x-z), data)) for z in range(min(data), max(data)+1)]))
    print ("Part 2:", min([sum(map(lambda x: abs(abs(x-z) * (1 + abs(x-z)) / 2), data)) for z in range(min(data), max(data)+1)]))
   # print(f"{tmp_sort} is this long: {len(tmp_sort)}")
   # if len(tmp_sort) % 2 == 0:
   #     # Even
   #     tmp = int(len(tmp_sort)/2)
   #     tmp2 = tmp+1
   #     med = int((tmp_sort[tmp] + tmp_sort[tmp2]) / 2)
   #     if med not in tmp_sort:
   #         med = tmp_sort[med]
   # else:
   #     # Odd
   #     med = tmp_sort[int(math.ceil(len(tmp_sort)/2))]
   # #mean = math.ceil(sum(tmp_sort)/len(tmp_sort))
   # mean = sum(tmp_sort)/len(tmp_sort)

   # options = []
   # tmp = []
   # for place in range(left, right+1):
   #     fuel = 0
   #     for crab in crabs:
   #         tmp_fuel = 0
   #         diff = int(abs(crab - place))
   #         if diff > 1:
   #             for counter in range(1,diff+1):
   #                 tmp_fuel += 1 * counter
   #         else:
   #             tmp_fuel += 1
   #         #print(f"{crab} to {place} == {diff} which cost: {tmp_fuel}")
   #         fuel += tmp_fuel
   #     options.append((place, fuel))
   #     tmp.append(fuel)

   # print(min(tmp))
   # print(min(options, key=lambda x: (x[1], -x[0])))


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
