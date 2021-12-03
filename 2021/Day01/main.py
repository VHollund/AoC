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

def day_1_1(data):
    inc=0
    dec=0
    for x in range(len(data)):
        if data[x]>data[x-1]:
            inc+=1
    print(inc)

def day_1_1(data):
    inc=0
    for x in range(len(data)):
        if x+3>len(data)-1:
            break
        if data[x]+data[x+1]+data[x+2]<data[x+1]+data[x+2]+data[x+3]:
            inc+=1
    print(inc)

if __name__ == '__main__':
    data = get_input_split_lines(2021, "01")
    data = sanitize(data)
    print(data)
    day_1_1(data)
