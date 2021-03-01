def recherche_iter(tab, nombre):

	if tab == []:
		print("le tableau est vide")

	else: 
		var = 'test'

		for i in range (0, len(tab)):
			if tab[i] == nombre:
				var = i

		if var == str:
			print("l element recherche n est pas dans le tableau")

		else:
			print("l element est present dans le tableau avec pour dernier indice " + str(var))

recherche_iter([1,2,3,4,5,1],2) #len = 3