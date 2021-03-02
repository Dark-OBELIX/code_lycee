def tri (tab):

    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i = i + 1

        else:
            valeur = tab[j]
            tab[j] = 1
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1

    return tab

tri([0,1,0,1,0,1,0,1,0])
# doit retourner [0, 0, 0, 0, 0, 1, 1, 1, 1]