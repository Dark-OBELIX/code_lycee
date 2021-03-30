def moyenne(tab):
    if not tab:
        print("erreur")
    else:
        somme = 0
        for i in tab:
            somme += i
        res = somme / len(tab)
        return res

moy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(moyenne(moy))
