def tri_bulles(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

T = [4, 10, 2, 1, 6, 5, 7]
print(tri_bulles(T))
