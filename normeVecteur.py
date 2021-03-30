from math import sqrt 

def normeVecteur():
    a = []
    x = float(input("Donne le point x : "))
    a.append(x)
    y = float(input("Donne le point y : "))
    a.append(y)
    z = float(input("Donne le point z : "))
    a.append(z)
    print(a)
    na = sqrt(a[0]**2 + a[1]**2 + a[2]**2)

    print("La norme est :", na)

normeVecteur()
