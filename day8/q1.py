import math

def calc_paint(w,h):
    return math.ceil((w*h)/5)


print(calc_paint(h=3,w=9))