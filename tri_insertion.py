def tri_insertion(L):

	n = len(L)
	#cas d'un tableau vide
	if n == 0:
		return L

	for j in range(1, n):
		e = L[j]
		i = j

		while i > 0 and L[i-1] > L[j]:
			i = i - 1
		if i != j:
			for k in range (j,i,-1):
				L[k] = L[k - 1]
	
			L[i] = e
	return L

############################################################

print(tri_insertion([10,9,8,7,6,5,4,3,2,1])) 

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
