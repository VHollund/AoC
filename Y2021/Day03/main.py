from Helpers.GetInput import get_input_split_lines

def sanitize(data):
    nd=[]
    for x in data:
        removeNL=x.replace("\n", "")
        nd.append(removeNL)
    return nd



def day_3_2_2(data,bit):
    newData = []
    common = 0
    common=0
    for x in data:
        common += int(x[bit])
    if common >= len(data)/2:
        common = 1
    else:
        common = 0
    for x in data:
        if int(x[bit]) == common:
            newData.append(x)
    if(len(data)>2):
        return day_3_2_2(newData, bit+1)
    return data


def day_3_2(data,bit):
    newData = []
    common = 0
    for x in data:
        common += int(x[bit])
    if common >= len(data)/2:
        common = 0
    else:
        common = 1
    for x in data:
        if int(x[bit]) == common:
            newData.append(x)
    if(len(data)>1):
        return day_3_2(newData, bit+1)
    return data



def day_3_1(data):
    gamma = ""
    eps = ""
    pos={}
    for x in data:
        for i in range(len(x)):
            if i in pos:
                pos[i] += int(x[i])
            else:
                pos[i] = int(x[i])
    print(len(data))
    for x,y in pos.items():

        if y > len(data)/2:
            gamma+="1"
            eps+="0"
            print(f"{x}:{1}")
        else:
            eps+="1"
            gamma+="0"
            print(f"{x}:{0}")
    print(int(gamma, 2)*int(eps, 2))

if __name__ == "__main__":
    data = get_input_split_lines(2021, "03")
    data = sanitize(data)
    day_3_1(data)
    print(day_3_2_2(data, 0))
    print(day_3_2(data, 0))
    x=int(day_3_2(data, 0)[0], 2)
    z=int(day_3_2_2(data, 0)[0], 2)
    print(z*x)
#13271449 too high
#13242321 too high
#13256877
#13256877
#13271449
#5285898 too high
#3368358