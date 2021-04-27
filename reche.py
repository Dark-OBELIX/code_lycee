def recherche(tab):

	reponse = []

	for i in range(0, len(tab) - 1):

		if tab[i] == (tab[i + 1] - 1):

			tab_temp = [tab[i],tab[i + 1]]	
			reponse.append(tab_temp)

	return reponse

###############################################################

#print(recherche([1,4,3,5]))
#[]

#print(recherche([1,4,5,3]))
#[[4, 5]]

#print(recherche([7,1,2,5,3,4]))
#[[1, 2], [3, 4]]

#print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))
#[[1, 2], [2, 3], [-5, -4]]