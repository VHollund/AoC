import typing

from Helpers.GetInput import get_input_split_lines
res={'X':0,'Y':3,'Z':6}

def getWinningMove(move):
    match move:
        case 1:return 2
        case 2:return 3
        case 3:return 1
        case _:print("ERROR")

def getLoosingMove(move):
    match move:
        case 1: return 3
        case 2: return 1
        case 3: return 2
        case _: print("ERROR")


def getScore(dataIn) -> int:
    if getWinningMove(ord(dataIn[0])-64) == ord(dataIn[1])-87:
        return (getWinningMove(ord(dataIn[0])-64))+6
    elif getLoosingMove(ord(dataIn[0])-64) == ord(dataIn[1])-87:
        return getLoosingMove(ord(dataIn[0])-64)
    else:
        return ord(dataIn[0])-64 + 3

def part1(data):
    score=0
    for x in data:
        score += getScore(x)
    print(score)


def part2(data):
    score=0
    for x in data:
        match x[1]:
            case 'Y': score += ord(x[0])-64+3
            case 'X': score += (getLoosingMove(ord(x[0])-64))+res[x[1]]
            case 'Z': score += (getWinningMove(ord(x[0])-64))+res[x[1]]
    print(score)


def day2():
    print(ord('Z')-87)
    data = get_input_split_lines(2022, "02")
    processed = []
    score = 0
    for x in data:
        y = x.replace("\n", "")
        y = y.split(" ")
        processed.append(y)
    part1(processed)
    part2(processed)


if __name__ == "__main__":
    day2()
