def fibonacci(valeur):
    lastval = 1
    lastval2 = 1
    newN=0
    i=0

    while i <= valeur:
        newN = lastval+lastval2
        lastval2 = lastval
        lastval = newN
        i+=1
    return newN