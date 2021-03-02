def multiplication(nombre_1, nombre_2):

    var_resultat = 0

    if nombre_1 > 0:
        for i in range (1, nombre_1 + 1):
            var_resultat = var_resultat + nombre_2
        print(var_resultat)

    elif nombre_2 > 0:
        for i in range (1, nombre_2+ 1):
            var_resultat = var_resultat + nombre_1
        print(var_resultat)

    else:
        nombre_1 = abs(nombre_1)
        nombre_2 = abs(nombre_2)
        for i in range(1, nombre_2 + 1):
            var_resultat = var_resultat + nombre_1
        print(var_resultat)


multiplication(-7,-5)