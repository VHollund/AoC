import re
import os

class square():
    def __init__(self,id ,x,y,l,h):
        self.id=id
        self.x=x
        self.y=y
        self.l=l
        self.h=h


squares=[]
pattern="([#])([0-9]*)\s[@]\s([0-9]*)[,]([0-9]*)[:]\s([0-9]+)x([0-9]+)[\s]?"
clear = lambda: os.system('clear')


def get_by_pos(x,y):
    matches=[]
    for k in squares:
        if k.x <= x and (k.x+k.l)>=x and k.y <= y and (k.y+k.h)>=y:
            matches.append(k)
    return matches


def get_dimensions():
    highX=0
    highY=0
    for s in squares:
        if (s.x+s.l)>highX:
            highX=(s.x+s.l)
        if (s.y + s.h) > highY:
            highY = (s.y + s.h)
    return [highX,highY]


def find_intersection():
    for x in squares:
        found=False
        intersection=False
        start=[x.x, x.y]
        end=[x.x+x.l,x.y+x.h]
        for z in range(start[0],end[0]):
            for l in range(start[1],end[1]):
                if len(get_by_pos(l,z)) > 1:
                    intersection=True
            if intersection:
                break
        if not intersection:
            return x.id



def solve():
    x=0
    tot=0
    with open("input.txt", "r") as input:
        for line in input:
            m = re.search(pattern,line)
            id=int(m.group(2))
            z=int(m.group(3))
            y=int(m.group(4))
            l=int(m.group(5))
            h=int(m.group(6))
            squares.append(square(id, z, y, l-1, h-1))
    dimesions = get_dimensions()
    total=dimesions[0]*dimesions[1]
    all=""
    for y in range(0,dimesions[1]+2):
        for n in range(0,dimesions[0]+2):
            pos=get_by_pos(n,y)
            if len(pos)>1:
                x+=1
                all+="X"
            elif len(pos)==1:
                all+="O"
            else:
                all+="."
            tot+=1
        all+="\n"
        clear()
        print(f"X:{dimesions[0]},Y:{dimesions[1]}, Total: {total}")
        print(f"{int(tot / total * 100)}%")
        print(x)
    clear()
    print(f"{int(tot / total * 100)}%")
    print(x)
    with open("output.txt","w+") as out:
        out.write(all)
    print(find_intersection())




def main():
    print("start")
    solve()


if __name__=="__main__":
    main()

