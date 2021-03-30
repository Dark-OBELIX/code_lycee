def convertir(T):
    n = 0
    for i in range(0, len(T)):
        n = 2*n + T[i]
    return n

T = [1, 0, 0, 0, 0, 0, 1, 0]        
print(convertir(T))
