def tri_selection(tab):
    n = len(tab)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if tab[min] > tab[j]:
                min = j
                    
        temp = tab[i]
        tab[i] = tab[min]
        tab[min] = temp

    return tab
    

t = [1, -52, -6, 9, 12]
print(tri_selection(t))
