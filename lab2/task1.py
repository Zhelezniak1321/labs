import math


def f(x):
    if x < 2:
        return 1 / math.sin(math.exp(x))
    elif 2 <= x < 3:
        return 1 / math.cos(math.log(x))
    else:
        return math.sin(math.log(x))

h = 0.2
a = 1.5
b = 3.5

x = 1.5
while  a <= x <= b:  
    print(round(x, 1), f(x))
    x += h
    x = round(x, 2)