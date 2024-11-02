import math

def S(x):
    result = 0
    k = 1  
    while True:
        if k != 1:  
            term = ((-1)**k * math.cos(k * x)) / (k**2 - 1)
            result += term
            if abs(term) < 0.001:  
                break
        k += 1  
    return round(result, 5)

x = -1
while x <= -0.9:
    print(x, S(x))  
    x +=round(0.001) 