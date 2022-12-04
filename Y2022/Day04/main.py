from Helpers.GetInput import *
import re


def part1(data):
    counter = 0
    for x in data:
        if (x[0] <= x[2] and x[1] >= x[3]) or (x[2] <= x[0] and x[3] >= x[1]):
            counter += 1
    print(counter)


def part2(data):
    counter = 0
    for x in data:
        if x[0] <= x[2] <= x[1] or x[2] <= x[0] <= x[3]:
            counter += 1
    print(counter)


def Day4():
    data = get_input_split_lines(2022, "04")
    pairs = []
    for x in data:
        pairs.append([int(x.strip()) for x in re.split("[,-]", x)])
    part1(pairs)
    part2(pairs)


if __name__ == "__main__":
    Day4()
