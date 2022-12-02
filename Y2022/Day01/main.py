from Helpers.GetInput import get_input_split_lines

def day1():
    data = get_input_split_lines(2022, "01")
    processed = []
    last = []
    for x in data:
        if x == "\n":
            processed.append(last)
            last = []
            continue
        x.replace('\n', "")
        last.append(int(x))
    processed.append(last)
    print(processed)
    final = [sum(z) for z in processed]
    final.sort()
    print(sum(final[:-4:-1]))

if __name__ == "__main__":
    day1()
