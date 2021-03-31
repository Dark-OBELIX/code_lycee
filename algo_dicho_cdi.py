a = -1
b = 1

def fonction(x):
    res = x**3-3*x+1
    return res

while b - a > 10**(-1):
    m = (a+b)/2
    if (fonction(a) * fonction(m)) < 0:
        b = m
    else:
        a = m

print(m)