def moyenne(tableau_note):
    
    if len(tableau_note) == 0:
        print("Il n'y a pas de notes dans le tableau")

    else:
        var_moyenne = 0
        var_suivi = 0
        for i in range (0, len(tableau_note)):
            var_moyenne = var_moyenne + tableau_note[i]
            var_suivi = var_suivi + 1

        var_moyenne = var_moyenne / var_suivi
        print("La moyenne du tableau est " + str(var_moyenne))

moyenne([1,2,3,4])