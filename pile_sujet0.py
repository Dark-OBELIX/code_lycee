def creer_pile_vide():
    pile = []
    return pile

def depiler(liste):
    nombre_d = liste.pop()
    return nombre_d

def empiler(liste, nombre):
    nombre_e = liste.append(nombre)

def est_vide(liste):
    if liste:
        return True
    else:
        return False

def hauteur_pile (P):
    Q = creer_pile_vide()
    n = 0
    while not (est_vide(P)):
        n = n + 1
        x = depiler(P)
        empiler(Q, x)
    while not (est_vide(Q)):
        x = depiler(Q)
        empiler(P, x)
    return n

def retourner(P, i):
    Q = creer_pile_vide()
    R = creer_pile_vide()
    for nombre in range(0, i):
        x = depiler(P)
        empiler(Q, x)
    for nombre in range(len(Q)):
        x = depiler(Q)
        empiler(R, x)
    for nombre in range(len(R)):
        x = depiler(R)
        empiler(P, x)

def max_pile(P, i):
    #assert i <= hauteur_pile
    rang_maxi = 1
    maxi = depiler(P)
    rang = 2
    Q = creer_pile_vide()
    empiler(Q, maxi)
    while rang <= i:
        x = depiler(P)
        if x > maxi:
            maxi = x
            rang_maxi = rang
        empiler(Q, x)
        rang = rang + 1
    while not (est_vide(Q)):
        empiler(P, depiler(Q))
    return rang_maxi
######################################################################################################""

def tri_crepes(P):
    y = len(P) - 1
    while y != 0:
        print(P)
        x = max_pile(P, y)
        retourner(P, x)
        y = y - 1
    return P

P = [7,14,12,5,8]
tri_crepes(P)