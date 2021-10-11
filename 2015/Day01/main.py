from Helpers.GetInput import *

def day_1_1(data):
    floor=0
    for x in data[0]:
        if x=="(":
            floor+=1
        else:
            floor-=1
    print(floor)

def day_1_2(data):
    floor=0
    goal=-1
    for x in enumerate(data[0]):
        if x[1]=="(":
            floor+=1
        else:
            floor-=1
        if floor==goal:
            print(x[0]+1)
    print(floor)


if __name__ == '__main__':
    data=get_input_input_joined(2015, "01")
    print(data)
    day_1_2(data)