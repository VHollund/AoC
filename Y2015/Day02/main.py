from Helpers.GetInput import *

def get_area(l,w,h):
    sides=[l*w, w*h, h*l]
    sides.sort()
    return (sum(sides)*2)+sides[0]

def get_ribbon_length(l,w,h):
    sides=[l,w,h]
    sides.sort()
    return 2*sides[0]+2*sides[1]+l*w*h


def day_2_1(data):
    sum=0
    for x in data:
        k=x.replace("\n","").split("x")
        print(k)
        sum += get_area(int(k[0]),int(k[1]),int(k[2]))
    print(sum)

def day_2_2(data):
    sum=0
    for x in data:
        k=x.replace("\n","").split("x")
        print(k)
        sum += get_ribbon_length(int(k[0]),int(k[1]),int(k[2]))
    print(sum)


if __name__ == '__main__':
    data=get_input_split_lines(2015,"02")
    print(data)
    day_2_2(data)

#4425700 too high