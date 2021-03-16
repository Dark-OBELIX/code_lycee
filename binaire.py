def convertir(T):

	var_resultat = 0
	var_suivi = 0
	var_ini = len(T) - 1

	for i in range (0, len(T)):
		if T[var_ini] == 1:
			var_resultat = var_resultat + 2**var_suivi

		var_suivi = var_suivi + 1
		var_ini = var_ini - 1
	
	return var_resultat

###################################################################################

def convertir_2(T):
    n = 0
    for i in range(0, len(T)):
        n = 2*n + T[i]
    return n

###################################################################################

print(convertir([1,0,1,0,0,1,1]))

