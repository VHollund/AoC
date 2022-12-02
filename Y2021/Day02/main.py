def get_input_split_lines(year,day):
    with open(f'{year}\Day{day}\input.txt', 'r') as input:
        lines = input.readlines()
        return lines

def sanitize(data):
    data2=[]
    for x in data:
        x=x.replace("\n", "")
        x=int(x)
        data2.append(x)
    return data2



def day_2_1(data):
    map = {}
    for x in data:
        removeNL=x.replace("\n","")
        split=removeNL.split(" ")
        if split[0] in map:
            map[split[0]]+=int(split[1])
        else:
            map[split[0]] = int(split[1])
    print(map)
    print((map["down"]-map["up"])*map["forward"])


def day_2_2(data):
    aim=0
    dep=0
    hor=0
    for x in data:
        removeNL = x.replace("\n", "")
        split = removeNL.split(" ")
        if split[0]=="down":
            aim+=int(split[1])
        if split[0] == "up":
            aim -= int(split[1])
        if split[0] == "forward":
            hor+=int(split[1])
            dep+=aim*int(split[1])
    print(hor*dep)


if __name__ == '__main__':
    data = get_input_split_lines(2021, "02")
    day_2_1(data)
    day_2_2(data)
