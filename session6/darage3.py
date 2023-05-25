import math
from os import _exit

def m_darage3(a = int, b = int, c = int, d = int):

    print("a*x^3 + b*x^2 c*x + d = 0")

    if a == 0 :
        print("a nimshe 0 bashe ")
        exit()

    e = b - (a^2)/3
    f = ((2*a^3)/27) - (a*b/3) + c

    delta = ((f**2)/4) + ((e**3)/27)

    if delta == 0 :
        ...
    elif delta > 0 :
        x = math.pow((-f/2) + math.sqrt(delta), (1/3)) + math.pow(((-f/2) - math.sqrt(delta)), (1/3)) - a/3

    elif delta < 0:
        ...            


m_darage3(8, 4, 6, 8)        