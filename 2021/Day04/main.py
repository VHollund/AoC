from Helpers.GetInput import get_input_split_lines

class board:
    def __init__(self):
        self.lines=[]

    def add_line(self,line):
        self.lines.append(line)

    def addNcheck(self,num):
        self.mark(num)
        if [self.check_vertical(),self.check_horizontal(),self.check_diag_left(),self.check_diag_right()].count(True)>1:
            return False
        return self.check_vertical() or self.check_horizontal() or self.check_diag_left() or self.check_diag_right()

    def check_horizontal(self):
        if ['x','x','x','x','x'] in self.lines:
            return True
        return False

    def check_vertical(self):
        found=True
        for x in range(len(self.lines)):
            for z in self.lines:
                if z[x]!='x':
                    found=False
                    break
            if found:
                return True
            found=True
        return False

    def check_diag_left(self):
        for x in range(len(self.lines)):
            if self.lines[x][x]!='x':
                return False
        return True

    def check_diag_right(self):
        for x in range(len(self.lines)):
            if self.lines[len(self.lines)-1-x][x] != 'x':
                return False
        return True

    def mark(self, number):
        for x in self.lines:
            for z in range(len(x)):
                if x[z]==number:
                    x[z]='x'

    def sum_unmarked(self):
        sum=0
        for x in self.lines:
            for z in x:
                if z!='x':
                    sum+=z
        return sum

    def print(self):
        for x in self.lines:
            print(x)


if __name__ == "__main__":
    boards=[]
    data = get_input_split_lines(2021, "04")
    nums=[int(x) for x in data[0].replace("\n","").split(",")]
    data.pop(0)
    print(data)
    k = ""
    for x in data:
        if x=='\n':
            if k!="":
                boards.append(k)
            k=board()
        else:
            l=x.replace("\n","").replace("  "," ").split(" ")
            if '' in l:
                l.remove('')
            k.add_line([int(x) for x in l])
    pass
    for x in nums:
        for z in range(len(boards)):
            if boards[z].addNcheck(x):
                print(boards[z].sum_unmarked()*x)
                boards[z].print()

