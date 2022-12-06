from Helpers.GetInput import *


def part1(data):
	for x in range(4, len(data)):
		if len(set(data[x-4:x])) == 4:
			print(x)
			break


def part2(data):
	for x in range(14, len(data)):
		if len(set(data[x - 14:x])) == 14:
			print(x)
			break


def Day6():
	data = get_input_split_lines(2022, "06")[0]
	part1(data)
	part2(data)


if __name__ =="__main__":
	Day6()
