def moyenne(T):

	calcul_haut = 0
	calcul_bas = 0

	for i in range (0, len(T)):
		for j in range (0, 1):

			var = T[i][j]
			var_2 = T[i][1]

			calcul_haut = calcul_haut + var * var_2
			calcul_bas = calcul_bas + var_2

	return calcul_haut / calcul_bas

############################################################

print(moyenne([(15,2),(9,1),(12,3)]))
