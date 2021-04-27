def nbLig(image):
    return len(image)

def nbCol(image):
    return len(image[0])

def negatif(image):

    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(len(image)):

        for j in range(len(image[0])):

            L[i][j] = 255 - image[i][j]

    return L

def binaire(image, seuil):

    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    
    for i in range(len(image)):

        for j in range(len(image[i])):

            if image[i][j] < seuil :
                L[i][j] = 0

            else:
                L[i][j] = 1

    return L

#############################################################################################
img=[[20, 34, 254, 145, 6], [23, 124, 287, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]

#print(nbLig(img))
# 4

#print(nbCol(img))
# 5

#print(negatif(img))
# [[235, 221, 1, 110, 249], [232, 131, -32, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]

#print(binaire(img,120))
# [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]