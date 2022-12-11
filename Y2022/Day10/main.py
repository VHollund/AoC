from Helpers.GetInput import *

cycleList= [20,60,100,140,180,220]



def part1(data):
	sigstrenghtSum = 0
	X=1
	cycle=1
	for x in data:
		k=x.split(" ")
		if k[0] == "addx":
			cycle += 1
			if cycle in cycleList:
				print(f"cycle#{cycle}: {X}")
				sigstrenghtSum+=X*cycle
			X+=int(k[1].strip())
		cycle+=1
		if cycle in cycleList:
			print(f"cycle#{cycle}: {X}")
			sigstrenghtSum += X*cycle
	print(sigstrenghtSum)

def pixelpos(cycle):
	p=cycle
	line=0
	while p>40:
		line+=1
		p-=40
	return line, p-1


def printPixels(pixels):
	for x in pixels:
		print(x)


def part2(data):
	pixels=["" for _ in range(8)]
	X = 1
	cycle = 1
	line=0
	pp=0
	pixels[0]+="#"
	for x in data:
		k = x.split(" ")
		if k[0] == "addx":
			cycle += 1
			line, pp = pixelpos(cycle)
			if X-1<= pp <=X+1:
				pixels[line] += "#"
			else:
				pixels[line] += "."
			X += int(k[1].strip())
		cycle += 1
		line, pp = pixelpos(cycle)
		if X - 1 <= pp <= X + 1:
			pixels[line] += "#"
		else:
			pixels[line] += "."
	printPixels(pixels)


def Day10():
	data = get_input_split_lines(2022,"10")
	print(pixelpos(1),pixelpos(40))
	print(pixelpos(41), pixelpos(80))
	part1(data)
	part2(data)


if __name__ =="__main__":
	Day10(None)
