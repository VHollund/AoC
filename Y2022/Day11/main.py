import typing
from functools import reduce

from Helpers.GetInput import *


class monkey():
    def __init__(self, id, items, divNumber, OM, operator, opNum, true, false):
        self.id:int = id
        self.items: typing.List[int] = []
        self.otherMonkeys: typing.List[monkey] = OM
        self.test:int = divNumber
        self.operator:str = operator
        self.opNum: int = opNum
        self.sendIfFalse = false
        self.sendIftrue = true
        self.newitems: typing.List[int] = items
        self.inspectedItem = 0

    def run(self, worrydivider=3):
        self.items = self.newitems
        self.newitems = []
        for x in range(len(self.items)):
            item = self.items[x]
            if self.operator == "*":
                item *= self.opNum
            elif self.operator == "**":
                item = item ** self.opNum
            else:
                item += self.opNum
            if worrydivider==3:
                item //= worrydivider
            else:
                item %= worrydivider
            self.inspectedItem += 1
            otherMonkey = self.otherMonkeys[self.sendIftrue if item % self.test == 0 else self.sendIfFalse]
            otherMonkey.newitems.append(item)
        self.items = []

    def __str__(self):
        return f"Monkey {self.id}: {self.newitems} and inspected items {self.inspectedItem} times."


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def parseMonkeys(data) -> typing.List[monkey]:
    monkeylist: typing.List[monkey] = []
    with open(data) as f:
        data = "".join(f.readlines()).split("\n\n")
        for x in data:
            y = x.split("\n")
            d0 = int(y[0].split(" ")[1][0:1])
            d1 = [int(l) for l in y[1].split(": ")[1].split(",")]
            d2 = y[2].split("new = old ")[1].split(" ")
            if d2 == ["*", "old"]:
                d2 = ["**", 2]
            d3 = int(y[3].split("divisible by ")[1])
            d4 = int(y[4].split("throw to monkey ")[1])
            d5 = int(y[5].split("throw to monkey ")[1])
            monkeylist.append(monkey(d0, d1, d3, monkeylist, d2[0], int(d2[1]), d4, d5))
    return monkeylist
#(id, items, divNumber, OM, operator, opNum, true, false):


def part1(data):
    monkeylist: typing.List[monkey] = parseMonkeys(data)
    for _ in range(20):
        for x in monkeylist:
            x.run()
    for x in monkeylist:
        print(x)
    monkeylist.sort(key=lambda x: x.inspectedItem, reverse=True)
    print(f"part1: {monkeylist[0].inspectedItem * monkeylist[1].inspectedItem}")



def part2(data):
    monkeylist: typing.List[monkey] = parseMonkeys(data)
    divisorLimit=reduce(lambda c, m: c * m.test, monkeylist, 1)
    for x in range(10000):
        print(x)
        for z in monkeylist:
            z.run(divisorLimit)
    for x in monkeylist:
        print(x)
    monkeylist.sort(key=lambda x: x.inspectedItem, reverse=True)
    print(f"part2: {monkeylist[0].inspectedItem * monkeylist[1].inspectedItem}")


def Day11():
    part1("Y2022/Day11/input.txt")
    part2("Y2022/Day11/input.txt")


if __name__ == "__main__":
    Day11()
