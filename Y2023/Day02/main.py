from Helpers.GetInput import *
import re

limits = {"red": 12, "green": 13, "blue": 14}

def get_id_and_games(line):
	split=line.split(":")
	id=int(split[0].split(" ")[1])
	return int(id), split[1]


def valid_game(game):
	k = []
	for x in re.findall(r"\s?([0-9]+)\s([red]{3}|[gren]{5}|[blue]{4})[,]?", game):
		if int(x[0]) <= limits[x[1]]:
			k.append(True)
		else:
			k.append(False)
			break
	return all(k)


def game_power(game):
	min_values = {'red': 0, 'green': 0, 'blue': 0}
	for x in re.findall(r"\s?([0-9]+)\s([red]{3}|[gren]{5}|[blue]{4})[,]?", game):
		if int(x[0]) >= min_values[x[1]]:
			min_values[x[1]] = int(x[0])
	return min_values['red'] * min_values['green'] * min_values['blue']


def part1(data):
	games=[]
	for x in data:
		current = get_id_and_games(x)
		if valid_game(current[1]):
			games.append(current[0])
	print(sum(games))


def part2(data):
	games = []
	for x in data:
		current = get_id_and_games(x)
		games.append(game_power(current[1]))
	print(sum(games))


def day():
	data = get_input_split_lines(2023, "02")
	part1(data)
	part2(data)


if __name__ =="__main__":
	day()
