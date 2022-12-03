from Helpers.GetInput import *

def findBadge(group):
	for x in group[0]:
		if x in group[1] and x in group[2]:
			print(x)
			return x

def chunks(l, n):
	for i in range(0, len(l), n):
		yield l[i:i+n]

def part1(data):
	pri = 0
	for backpack in data:
		comp1 = backpack[:int(len(backpack)/2)]
		comp2 = backpack[int(len(backpack)/2):]
		for item in comp1:
			if item in comp2:
				if item.isupper():
					pri += ord(item)-38
				else:
					pri += ord(item)-96
				break
	return pri

def part2(data):
	pri=0
	for x in chunks(data,3):
		badge = findBadge(x)
		if badge.isupper():
			pri += ord(badge) - 38
		else:
			pri += ord(badge) - 96
	print(pri)

def Day3():
	data = get_input_split_lines(2022, "03")
	for x in range(len(data)):
		data[x]=data[x].replace("\n", "")
	print(part1(data))
	part2(data)


if __name__ =="__main__":
	Day3()
