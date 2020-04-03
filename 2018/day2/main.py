dict={}

def solve():
    print("getting input")
    with open("input","r") as input:
        for line in input:
            lettercount=[]
            for x in line:
                lettercount.append(line.count(x))
            lettercount.sort()
            print(set(lettercount))
            for x in set(lettercount):
                if x in dict:
                    dict[x]=dict[x]+1
                else:
                    dict[x] = 1
    print(dict)
    print(dict[2]*dict[3])



def main():
    print("start")
    solve()

if __name__=="__main__":
    main()