import sys, time

Attr = {
    'Reset': 0,
    'Bold': 1,
    'Underline': 4,
    'Blink': 5,
    'Reverse': 7,
    'Hidden': 8,
    'Black': 30,
    'Red': 31,
    'Green': 32,
    'Yellow': 33,
    'Blue': 34,
    'Purple': 35,
    'Cyan': 36,
    'White': 37
}

_getstamp = lambda f:time.strftime(f, time.localtime())

#Redefine the print function
def print(rstr:str, *attr):
    fstr = '\033[%sm'
    attr = ';'.join([str(Attr[a]) for a in attr])
    sys.stdout.write(f"{fstr%attr}{rstr}{fstr%Attr['Reset']}\n")
