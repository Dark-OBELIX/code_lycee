possibilite = [500,200,100,50,20,10,5,2,1]
total = 753
solution=[]

def rendu_pieces_recur(somme,S,pieces_rendues,ind):
	
	# fin du programme
	if somme == 0:
		print (pieces_rendues)

	elif S[ind] <= somme:
		somme = somme - S[ind]
		ind = ind + 1
		print(somme)
		return rendu_pieces_recur(somme,S,pieces_rendues,ind) # faut jouer avec les valeurs dans c'est parenthèses
		
	elif ind == len(S)-1:
		print("elif 2")
		ind = ind + 1
		return ind 

	else:
		print("else")
		print (pieces_rendues)

rendu_pieces_recur(total,possibilite,solution,0)