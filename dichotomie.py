def dichotomie(tab, x):
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

liste = [10, 12, 14, 15, 16]
print(dichotomie(liste, 16))
