from Helpers.GetInput import get_input_input_joined
from time import perf_counter
def treat(data):
    x=[int(x) for x in data.split(",")]
    return x

def part1(data):
    fish = []
    new_fish = []
    day = 0
    for x in data:
        fish.append(x)
    while day < 80:
        for x in range(len(fish)):
            if fish[x] == 0:
                new_fish.append(8)
                fish[x] = 7
            fish[x] -= 1
        fish.extend(new_fish)
        new_fish = []
        print(f"Day {day} Finished")
        day += 1
    print(len(fish))

def part2quick(data):
    fishCounter={}
    newStatus={}
    for x in range(0,9):
        fishCounter[x]=data.count(x)
    for z in range(256):
        for x,y in fishCounter.items():
            if x==8:
                newStatus[x]=fishCounter[0]
            else:
                newStatus[x]=fishCounter[x+1]
                if x==6:
                    newStatus[x]+=fishCounter[0]
        fishCounter=newStatus
        newStatus={}
        print(fishCounter)
        print(sum(fishCounter.values()))
        print(f"finished day {z}")


if __name__ == "__main__":
    data=get_input_input_joined(2021,"06")[0]
    data=treat(data)
    #part1(data)
    st=perf_counter()
    part2quick(data)
    en=perf_counter()
    print(f"part 2 took {en-st} seconds")