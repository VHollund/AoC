import re

from Helpers.GetInput import *
pattern=r"^([a-zA-Z\s]*)([0-9]{0,3}),([0-9]{0,3})([a-zA-Z\s]*)([0-9]{0,3}),([0-9]{0,3})$"


def day_6_1(data):
    lights={}
    p=re.compile(pattern)
    for x in range(1000):
        for y in range(1000):
            lights[(x, y)] = False
    for line in data:
        result = p.search(line)
        if "turn off" in result.group(1):
            for y in range(int(result.group(3)), int(result.group(6))+1):
                for x in range(int(result.group(2)), int(result.group(5))+1):
                    lights[(x, y)] = False
        if "turn on" in result.group(1):
            for y in range(int(result.group(3)), int(result.group(6))+1):
                for x in range(int(result.group(2)), int(result.group(5))+1):
                    lights[(x, y)] = True
                pass
        if "toggle" in result.group(1):
            for y in range(int(result.group(3)), int(result.group(6))+1):
                for x in range(int(result.group(2)), int(result.group(5))+1):
                    lights[(x, y)] = not lights[(x, y)]
                    pass
    count = list(lights.values()).count(True)
    print(count)

def day_6_1(data):
    lights={}
    p=re.compile(pattern)
    for x in range(1000):
        for y in range(1000):
            lights[(x, y)] = 0
    for line in data:
        result = p.search(line)
        if "turn off" in result.group(1):
            for y in range(int(result.group(3)), int(result.group(6))+1):
                for x in range(int(result.group(2)), int(result.group(5))+1):
                    if lights[(x, y)] > 0:
                        lights[(x, y)] -= 1
        if "turn on" in result.group(1):
            for y in range(int(result.group(3)), int(result.group(6))+1):
                for x in range(int(result.group(2)), int(result.group(5))+1):
                    lights[(x, y)] += 1
                pass
        if "toggle" in result.group(1):
            for y in range(int(result.group(3)), int(result.group(6))+1):
                for x in range(int(result.group(2)), int(result.group(5))+1):
                    lights[(x, y)] += 2
                    pass
    count = sum(list(lights.values()))
    print(count)


if __name__ == '__main__':
    data = get_input_split_lines(2015, "06")
    day_6_1(data)
    print()