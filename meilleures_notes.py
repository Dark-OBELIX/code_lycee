listes_eleves = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meileures_notes():
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi = []

    for compteur in range(0, len(liste_notes)-1):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(listes_eleves[compteur])

        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [listes_eleves[compteur]]

    return (note_maxi, nb_eleves_note_maxi, liste_maxi)

################################################################

print(meileures_notes())
#(80, 3, ['c','f','h'])