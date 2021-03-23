b = []

def conv_bin(n):
    if n > 1:
        conv_bin(n // 2)
    b.append(n % 2)
    return b , len(b)

#################################################
print(conv_bin(9))
#([1, 0, 0, 1], 4)