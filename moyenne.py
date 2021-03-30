def moyenne(note):
    total = 0
    div = 0
    for element in note:
        total = total + element[0] * element[1]
        div = div + element[1]
    return total/div

notes = [(15, 2), (9, 1), (12, 3)]
print(moyenne(notes))
