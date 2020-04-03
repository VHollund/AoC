
values = []
seen={0}



def calculate(p1,found,tot):
    total=tot
    tot=total
    for x in values:
            total=total+int(x)
            if total in seen:
                print(total)
                found=True
                return
            seen.add(total)
    if not p1:
        print(total)
    if not found:
        calculate(True,found, total)

def get_input():
    with open("input.txt", "r") as file:
        for line in file:
            split = line.replace("\n", "")
            values.append(split)
    print(values)


def main():
    found = False
    get_input()
    calculate(False,found,0)

if __name__=="__main__":
    main()