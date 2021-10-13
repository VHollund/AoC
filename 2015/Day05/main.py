from Helpers.GetInput import *
import re
pattern = r"(\w*)?([a-z])([a-z])\2(\w*)?"
pattern2= r"(\w*)?([a-z]{2})(\w*?)\2(\w*)"


def doubles(word):
    for x in range(26):
        if (chr(ord('a') + x)*2) in word:
            return True
    return False


def forbidden_combos(word):
    forbidden = ["ab", "cd", "pq", "xy"]
    for x in forbidden:
        if x in word:
            return False
    return True

def vowels(word):
    letters = "aeiou"
    sum = 0
    for x in letters:
        sum += word.count(x)
    return sum > 2


def nice_word(word):
    return vowels(word) and forbidden_combos(word) and doubles(word)

def day_5_1(data):
    count = 0
    for x in data:
        if nice_word(x):
            count += 1
    print(count)


def day_5_2(data):
    f = re.compile(pattern)
    s = re.compile(pattern2)
    l1 = list(filter(f.match, data))
    l2 = list(filter(s.match, l1))
    print(len(l2))

#did part 2 using regex cuz i was bored
if __name__ == '__main__':
    data = get_input_split_lines(2015, "05")
    day_5_2(data)
    print()
