import re
from Helpers.GetInput import get_input_split_lines

pattern=r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"

class table():
    def __init__(self):
        self.tableGrid=[]
        for x in range(1000):
            self.tableGrid.append([])
            for z in range(1000):
                self.tableGrid[x].append(0)

    def fillLine_day1(self, start,end):
        if start[0]==end[0]:
            self.fillVertical(min(start[1],end[1]),max(start[1],end[1]),start[0])
        elif start[1]==end[1]:
            self.fillHorizontal(min(start[0],end[0]),max(start[0],end[0]),start[1])
        else:
            print(start,end="")
            print(end)
        return

    def fillDiagonal(self,start,end):
        step1 = 1 if start[0]<end[0] else -1
        step2 = 1 if start[1]<end[1] else -1
        x,y = start[0],start[1]
        while x!=end[0]+step1 and y!=end[1]+step2:
            self.tableGrid[y][x]+=1
            x+=step1
            y+=step2


    def fillLine_day2(self, start,end):
        if start[0]==end[0]:
            self.fillVertical(min(start[1],end[1]),max(start[1],end[1]),start[0])
        elif start[1]==end[1]:
            self.fillHorizontal(min(start[0],end[0]),max(start[0],end[0]),start[1])
        else:
            self.fillDiagonal(start,end)
        return

    def fillHorizontal(self,start,end,y):
        for x in range(start,end+1):
            self.tableGrid[y][x]+=1

    def fillVertical(self,start,end,x):
        for y in range(start, end+1):
            self.tableGrid[y][x] += 1

    def sum(self):
        s=0
        for x in self.tableGrid:
            s+=sum(x)
        return s

    def countOverlap(self):
        count=0
        for y in self.tableGrid:
            for x in y:
                if x>1:
                    count+=1
        return count

    def print(self):
        for y in self.tableGrid:
            print()
            for x in y:
                if x==0:
                    print(".",end="")
                else:
                    print(x,end="")

def treat(data):
    new_data=[]
    for x in data:
        k=re.match(pattern,x)
        new_data.append([int(x) for x in k.groups()])
    return new_data

def day_5_1(data):
    grid=table()
    for x in data:
        grid.fillLine_day1((x[0],x[1]),(x[2],x[3]))
    print(grid.countOverlap())
    #grid.print()

def day_5_2(data):
    grid=table()
    for x in data:
        grid.fillLine_day2((x[0],x[1]),(x[2],x[3]))
    print(grid.countOverlap())
    #grid.print()

if __name__ == "__main__":
    data=get_input_split_lines(2021,"05")
    data=treat(data)
    print(data)
    #day_5_1(data)
    day_5_2(data)

#1314 too low
#20200 too low
#too high 20318