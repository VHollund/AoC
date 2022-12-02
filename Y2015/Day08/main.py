from Helpers.GetInput import *
import re
import codecs


def day_8_1(data):
    tot_length = 0
    mem_length = 0
    for x in data:
        x=x[0:len(x)-1] #remove new line
        tot_length += len(x)
        x=x[1:len(x)-1] #remove starting and ending "
        mem_length += len(codecs.decode(x, 'unicode_escape'))
    print(tot_length-mem_length)


def day_8_2(data):
    tot_length=0
    mem_length=0
    for x in data:
        x=x[0:len(x)-1] #remove new line
        mem_length += len(x)
        x=x.replace("\\", "\\\\").replace('"', r'\"')
        tot_length += len(x)+2 #+2 for outer ""
    print(tot_length-mem_length)


if __name__ == '__main__':
    data = get_input_split_lines(2015, "08")
    day_8_1(data)
    day_8_2(data)