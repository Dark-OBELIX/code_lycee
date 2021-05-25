def longueur(xA, yA, xB, yB):
    return ((xB-xA)**2 + (yB-yA)**2)**0.5

def longTotal(points):
    somme = 0
    prem = True
    for key,value in points.items():
        if prem:
            previous = value
            prem = False
        else:
            somme+=longueur(previous[0], previous[1], value[0], value[1])
            previous = value
    return somme

points = {
    'A' : (-2,4),
    'B' : (1,-2),
    'C' : (3,7),
    'D' : (5,-3)
}

print("Longueur Totale :", longTotal(points))