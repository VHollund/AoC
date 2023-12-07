from Helpers.GetInput import *

digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def first_real_number(line: str) -> int:
    if line=="739\n":
        pass
    digits_index = {line.find(x): x for x in digits.keys() if x in line}
    for y,x in enumerate(line):
        if x.isdigit():
            digits_index[y] = x
    num = digits_index[min(digits_index.keys())]
    if num.isdigit():
        return num
    else:
        return digits[num]


def last_real_number(line: str) -> int:
    if line=="739\n":
        pass
    digits_index = {line.rfind(x): x for x in digits.keys() if x in line}
    for y,x in enumerate(line):
        if x.isdigit():
            digits_index[y] = x
    num = digits_index[max(digits_index.keys())]
    if num.isdigit():
        return num
    else:
        return digits[num]


def first_number(line: str):
    return [x for x in line if x.isdigit()][0]


def last_number(line: str):
    return [x for x in line if x.isdigit()][-1]


def part1(data):
    numbers = []
    for x in data:
        numbers.append(int(str(first_number(x)) + str(last_number(x))))
        print(f"'{x}'\nfirst number: {first_number(x)}\nsecond number: {last_number(x)}\nParsed: {8*' '}{numbers[-1]}")
    print(sum(numbers))


def part2(data):
    numbers = []
    for x in data:
        numbers.append(int(str(first_real_number(x)) + str(last_real_number(x))))
        print(
            f"'{x[:len(x)-1]}'\nfirst number:  {first_real_number(x)}\nsecond number: {last_real_number(x)}\nParsed: {7 * ' '}{numbers[-1]}\n")

    print(sum(numbers))


def day():
    data = get_input_split_lines(2023, "01")
    # Example data
    # data = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234","7pqrstsixteen"]
    # part1(data)
    part2(data)


if __name__ == "__main__":
    day()
