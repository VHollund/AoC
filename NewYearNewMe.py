import os

standard_setup=[
    "from Helpers.GetInput import *\n",
    "\n",
    "\n",
    "def part1(data):\n",
    "\tpass\n",
    "\n",
    "\n",
    "def part2(data):\n",
    "\tpass\n",
    "\n",
    "\n",
    'if __name__ =="__main__":\n',
    "\tpart1(None)\n",
    "\tpart1(None)\n"
]

def createFiles(dayString):
    if not os.path.isfile(os.path.join(dayString, "main.py")):
        with open(os.path.join(dayString, "main.py"), "w") as file:
            file.writelines(standard_setup)
    if not os.path.isfile(os.path.join(dayString, "input.txt")):
        with open(os.path.join(dayString, "input.txt"), "w") as file:
            file.writelines(["pass"])


def createSubFolder(year):
    for x in range(1, 26):
        if x<10:
            dayString=f'{year}/Day0{x}'
        else:
            dayString=f'{year}/Day{x}'
        if not os.path.exists(dayString):
            os.makedirs(dayString)
        createFiles(dayString)


def createYear(year):
    if not os.path.exists(year):
        os.makedirs(year)
    createSubFolder(year)

if __name__ == '__main__':
    createYear('2023')