from Helpers.GetInput import get_input_split_lines

def part1(data):
    sum=0
    for x in data:
        sum+=eval(x)
        print(sum)
    print(sum)

if __name__ == "__main__":
    data=get_input_split_lines(2020,"18")
    part1(data)