from Helpers.GetInput import *


def distance_up(x, y, data):
    if y == 0:
        return 0
    dist = 0
    z = data[0:y].copy()
    z.reverse()
    for tree in z:
        if tree[x] < data[y][x]:
            dist += 1
        elif tree[x] == data[y][x]:
            dist += 1
            break
    return dist


def distance_down(x, y, data):
    if y == len(data) - 1:
        return 0
    dist = 0
    for tree in data[y + 1:len(data) + 1]:
        if tree[x] < data[y][x]:
            dist += 1
        elif tree[x] == data[y][x]:
            dist += 1
            break
    return dist


def distance_left(x, y, data):
    if x == 0:
        return 0
    dist = 0
    z = data[y][0:x].copy()
    z.reverse()
    for tree in z:
        if tree < data[y][x]:
            dist += 1
        elif tree == data[y][x]:
            dist += 1
            break
    return dist


def distance_right(x, y, data):
    dist = 0
    if x==len(data[y])-1:
        return 0
    for tree in data[y][x+1:len(data[y])]:
        if tree < data[y][x]:
            dist += 1
        elif tree == data[y][x]:
            dist += 1
            break
    return dist


def hiddenTop(x, y, data):
    for tree in data[0:y]:
        if tree[x] >= data[y][x]:
            return True
    return False


def hiddenButtom(x, y, data):
    for tree in data[y + 1:len(data) + 1]:
        if tree[x] >= data[y][x]:
            return True
    return False


def hiddenLeft(x, y, data):
    if not data[y][0:x]:
        return False
    if max(data[y][0:x]) >= data[y][x]:
        return True
    return False


def hiddenRight(x, y, data):
    if not data[y][x + 1:len(data[y])]:
        return False
    if max(data[y][x + 1:len(data[y])]) >= data[y][x]:
        return True
    return False


def visible(x, y, data):
    top = hiddenTop(x, y, data)
    buttom = hiddenButtom(x, y, data)
    left = hiddenLeft(x, y, data)
    right = hiddenRight(x, y, data)
    return not all([top, buttom, left, right])


def scenery_score(x, y, data):
    return distance_up(x, y, data) * distance_down(x, y, data) * distance_left(x, y, data) * distance_right(x, y, data)


def part1(data):
    visibleTrees = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if visible(x, y, data):
                visibleTrees += 1
    print(visibleTrees)
    print(visible(97, 97, data))


def part2(data):
    scenery_scores = []
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            scenery_scores.append(scenery_score(x, y, data))
    print(max(scenery_scores))


def Day8():
    data = get_input_split_lines(2022, "08")
    for x in range(len(data)):
        data[x] = [int(x) for x in [*data[x].strip()]]
    part1(data)
    part2(data)


if __name__ == "__main__":
    Day8()

# p1 1708
# p2 504000
