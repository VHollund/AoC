from datetime import datetime
import re
import os

pattern = "[[]([0-9]*)[-]([0-9]*)[-]([0-9]*)\s([0-9]+)[:]([0-9]+)[]]\s([a-zA-Z\s#0-9]*)[\n]?"
clear = lambda: os.system('clear')
entries=[]


class entry():
    def __init__(self, year, month, day, hour, minute, action):
        self.time=datetime(year,month,day,hour,minute,)
        self.action=action

    def __str__(self):
        print(f"[{self.time}] {self.action}")

def solve():
    x=0
    tot=0
    with open("input.txt", "r") as input:
        for line in input:
            info=re.search(pattern,line)
            entries.append(entry(info.group(1),info.group(2),info.group(3),info.group(4),info.group(5),info.group(6)))

def main():
    print("start")
    solve()


if __name__=="__main__":
    main()
