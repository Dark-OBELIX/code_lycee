def tri_selection(T):
    n = len(T)
    for i in range(0,n-1):
        last_val = T[i]
        position = i
        for j in range(i+1,n):
            if last_val>T[j]:
                last_val = T[j]
                position = j
        T[position] = T[i]
        T[i] = last_val
    return T

##########################################################

print(tri_selection([9,2,5,1]))
# [1, 2, 5, 9]