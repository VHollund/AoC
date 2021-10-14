import copyreg
import re

from Helpers.GetInput import *

vars=r"^[\w\s]*->\s([a-z]{1,2})"

class wire:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.OverRide = False

    def print_value(self):
        print(f"{self.name}: {self.value}")

    def set_value(self, x):
        if not self.OverRide:
            self.value = x

    def set_not(self, x):
        if not self.OverRide:
            tmp = int("".join(['0' if x=='1' else '1' for x in '{0:16b}'.format(x)]), 2)
            self.value = tmp

    def rshift(self, x, y):
        if not self.OverRide:
            self.value = x >> y

    def lshift(self, x, y):
        if not self.OverRide:
            self.value = x << y

    def set_and(self, x, y):
        if not self.OverRide:
            self.value = int(x) & int(y)

    def set_or(self, x, y):
        if not self.OverRide:
            self.value = x | y

def validate_3part(sig,x,y):
    f = int(x) if x.isdigit() else sig[x].value
    s = int(y) if y.isdigit() else sig[y].value
    return f, s


def day_7_1(data):
    signals = {}
    st=re.compile(vars)
    first=True
    for x in data:
        z=st.match(x)
        if z is not None:
            signals[z.group(1)] = wire(z.group(1))
    while True:
        for x in data:
            x = x.replace("\n", "")
            parts = x.split(" ")
            if "LSHIFT" in x:
                v = validate_3part(signals, parts[0], parts[2])
                if v[0] is not None and v[1] is not None:
                    signals[parts[4]].lshift(v[0], v[1])
            elif "RSHIFT" in x:
                v = validate_3part(signals, parts[0], parts[2])
                if v[0] is not None and v[1] is not None:
                    signals[parts[4]].rshift(v[0], v[1])
            elif "AND" in x:
                v = validate_3part(signals, parts[0], parts[2])
                if v[0] is not None and v[1] is not None:
                    signals[parts[4]].set_and(v[0], v[1])
            elif "OR" in x:
                v = validate_3part(signals, parts[0], parts[2])
                if v[0] is not None and v[1] is not None:
                    signals[parts[4]].set_or(v[0], v[1])
            elif "NOT" in x:
                if parts[1].isdigit():
                    signals[parts[3]].set_not(parts[1])
                else:
                    if parts[1] in signals and signals[parts[1]].value is not None:
                        signals[parts[3]].set_not(signals[parts[1]].value)
            else:
                if parts[0].isdigit():
                    signals[parts[2]].set_value(int(parts[0]))
                elif parts[0] in signals and signals[parts[0]].value is not None:
                    signals[parts[2]].set_value(signals[parts[0]].value)
            if signals['a'].value is not None:
                signals['a'].print_value()
                signals['b'].set_value(signals['a'].value)
                signals['b'].OverRide = True
                for x,y in signals.items():
                    y.set_value(None)
                if not first:
                    exit(0)
                else:
                    first = False



if __name__ == '__main__':
    data = get_input_split_lines(2015, "07")
    day_7_1(data)
