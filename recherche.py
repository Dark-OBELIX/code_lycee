def recherche(liste, e):
    if liste:
        if e:
            count = 0
            for element in liste:
                if element == e:
                    ind = count
                count += 1
            return ind
        else:
            print("Aucun élément ne peut être recherché")
    else:
        print("Il n'y a pas de listes")

l = [1, 3, 4, 8, 11, 15, 3, 18, 3, 21]
print(recherche(l, 3))
