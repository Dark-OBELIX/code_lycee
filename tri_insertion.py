def tri_insertion(L):
    n = len(L)
    if L == []:
        return L
    for j in range(1, n):
        e = L[j]
        i = j
        while i > 0 and L[i-1] > L[j]:
            i -= 1
        if i != j:
            for k in range(j, i, -1):
                L[k] = L[k-1]
            L[i] = e
    return L

L = [2, 5, -1, 7, 0, 28]
print(tri_insertion(L))
