def fibonacci(valeur):
    lastval = 1
    lastval2 = 1
    newN=0
    i=0

    while i <= valeur:
        if i > 2:
            newN = lastval+lastval2
            lastval2 = lastval
            lastval = newN
        else:
            newN = 1
        i+=1
    return newN
