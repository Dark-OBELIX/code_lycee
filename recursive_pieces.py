def rendu_pieces_recur(somme, S, pieces_rendues=[], ind=0):
    if somme == 0:
        return pieces_rendues
    elif S[ind] <= somme:
        pieces_rendues.append(S[ind])
        return rendu_pieces_recur((somme-S[ind]), S, pieces_rendues, ind+1)
    elif ind == len(S)-1:
        return -1
    else:
        return rendu_pieces_recur(somme, S, pieces_rendues=[], ind=ind+1)

S = [500, 200, 100, 50, 20, 10, 5, 2, 1]
print(rendu_pieces_recur(7, S))
