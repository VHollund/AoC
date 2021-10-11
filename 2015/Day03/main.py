from Helpers.GetInput import *

class delivery:
    def __init__(self):
        self.x=0
        self.y=0

def day_3_1(data):
    houses={(0,0):1}
    x=0
    y=0
    count=0
    for z in data:
        if z=="^":
            y+=1
        elif z== "v":
            y-=1
        elif z== ">":
            x+=1
        elif z== "<":
            x-=1
        if (x,y) not in houses.keys():
            houses[(x,y)]=1
        else:
            houses[(x,y)]+=1
    print(houses)
    print(len(houses.keys()))

def day_3_2(data):
    houses={(0,0):2}
    santa=delivery()
    robot=delivery()
    current=None
    for z,c in enumerate(data,1):
        if z%2==0:
            current=santa
        else:
            current=robot

        if c=="^":
            current.y+=1
        elif c== "v":
            current.y-=1
        elif c== ">":
            current.x+=1
        elif c== "<":
            current.x-=1

        if (current.x,current.y) not in houses.keys():
            houses[(current.x,current.y)]=1
        else:
            houses[(current.x,current.y)]+=1
    print(houses)
    print(len(houses.keys()))

if __name__ == '__main__':
    data=get_input_input_joined(2015,"03")
    day_3_2(data[0])