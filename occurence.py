def occurences_lettres(phrase):
    dict_occ = {}
    for letter in phrase:
        if letter in dict_occ:
            dict_occ[letter] = int(dict_occ[letter]) + 1
        else:
            dict_occ[letter] = 1
    return dict_occ

phrase = "Hello World !"
print(occurences_lettres(phrase))
