def occurrence_max(chaine_caractere):

	alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	tab_result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	chaine_caractere_2 = chaine_caractere.lower()  # passage de toutes les lettres en minuscules
	liste = list(chaine_caractere_2) # je transforme mon mot en transforme tableau

	for i in range(0 ,len(liste)): # parcours pour toutes les lettres du mot qui est sous forme de tableau

		for j in range(0, 26): # parcours pour touters les lettres de l alphabet

			if liste[i] == alphabet[j]: # cas ou la lettre de l alphabet est egale a la lettre du mot
				tab_result[j] = tab_result[j] + 1

	max_occurence = max(tab_result)
	
	for l in range(0, 26):
		if tab_result[l] == max_occurence:
			print("max occurence = " + str(max_occurence) + " pour la lettre " + str(alphabet[l]))
			print(alphabet[l])

occurrence_max('je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique')