def dichotomie(tab, x):

    debut = 0
    fin = len(tab) - 1

    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True

        if x > tab[m]:
            debut = m + 1

        else:
            fin = m - 1

    return False

#dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
# True

#dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27)
# False
