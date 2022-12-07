import json
import re
from Helpers.GetInput import *
getFiles = False
dirSizes = {}
needed = 24933642


def get_sizes():
    print(sum([y for x, y in dirSizes.items() if y < 100000]))

def get_values(dictionary):
    values = []
    for key, value in dictionary.items():
        if isinstance(value, dict):
            values += get_values(value)
        else:
            values.append(value)
    return values


def summarize_directories(dictKey, data, currentPath):
    currsize=0
    for key, value in data.items():
        if type(value) == dict:
            currentPath.append(key)
            currsize += summarize_directories(key, value, currentPath)
            currentPath.pop()
        else:
            currsize += value
        if (type(data) == dict or type(value) == dict):
            if dictKey in dirSizes.keys():
                dirSizes[dictKey] += currsize
            else:
                dirSizes["/".join(currentPath)] = currsize
    return currsize


def folderExists(files, current, name):
    curr = files
    for x in current:
        curr = curr[x]
    if name in curr:
        return True
    else:
        createDir(files, current, name)
        return True


def createFiles(fileName, size, files, current):
    curr = files
    for x in current:
        curr = curr[x]
    curr[fileName] = int(size)


def createDir(files, current, name):
    curr = files
    for x in current:
        curr = curr[x]
    curr[name] = {}


def command(command, files, current, GF):
    global getFiles
    if getFiles:
        z = re.match(r"([0-9]+)\s([\w.]+)", command)
        if z:
            createFiles(z.group(2), z.group(1), files, current)
            return
        elif command.startswith("$"):
            GF[0] = False
    if command.startswith("$ cd"):
        if command[5:] == "..":
            current.pop()
        else:
            folderExists(files, current, command[5:])
            current.append(command[5:])
    elif command.startswith("$ ls"):
        getFiles = True


def part1(data):
    global total
    files = {"/": {}}
    current = []
    for x in data:
        command(x, files, current, [getFiles])
    summarize_directories("/", files, [])
    get_sizes()
    return files


def part2(data):
    needed=30000000-(70000000-sum(get_values(data)))
    key = min(dirSizes, key=lambda x: (dirSizes[x] - needed) if dirSizes[x] >= needed else float("inf"))
    print(key+":"+str(dirSizes[key]))


def Day7():
    data = get_input_split_lines(2022, "07")
    for x in range(len(data)):
        data[x] = data[x].strip()
    files=part1(data)
    part2(files)


if __name__ == "__main__":
    Day7()
