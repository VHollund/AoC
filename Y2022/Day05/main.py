import re
import typing

from Helpers.GetInput import *


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def getTop(stacks):
    for x in stacks:
        yield x[-1]


def part1(data, commands):
    for x in commands.split("\n"):
        mat = re.match(r"move\s([0-9]*)\sfrom\s([0-9]*)\sto\s(([0-9]*))", x)
        move9000(mat.group(1), mat.group(2), mat.group(3), data)
    print("".join(getTop(data)))


def part2(data, commands):
    for x in commands.split("\n"):
        mat = re.match(r"move\s([0-9]*)\sfrom\s([0-9]*)\sto\s(([0-9]*))", x)
        move9001(mat.group(1), mat.group(2), mat.group(3), data)
    print("".join(getTop(data)))


def move9000(mengde, fra, til, stacks):
    for x in range(int(mengde)):
        stacks[int(til) - 1].append(stacks[int(fra) - 1].pop())


def move9001(mengde, fra, til, stacks):
    stacks[int(til) - 1] += stacks[int(fra) - 1][-int(mengde):]
    stacks[int(fra) - 1] = stacks[int(fra) - 1][:-int(mengde)]


def structureData(rawData):
    stacks = []
    boxes = rawData.split("\n\n")[0]
    while len(stacks) < len(rawData.split("\n")[0]) / 4:
        stacks.append([])
    i = 0
    for x in chunks(boxes, 4):
        if ord('A') <= ord(x[1]) <= ord('Z'):
            stacks[i].append(x[1])
        i += 1
        if i == len(stacks):
            i = 0
    for i in range(len(stacks)):
        stacks[i].reverse()
    return stacks


def Day5():
    data = "".join(get_input_split_lines(2022, "05"))
    stacks = structureData(data)
    stacks2 = structureData(data)
    commands = data.split("\n\n")[1]
    part1(stacks, commands)
    part2(stacks2, commands)


if __name__ == "__main__":
    Day5()
