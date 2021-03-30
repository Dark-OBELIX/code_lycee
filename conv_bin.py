def conv_bin(n):
    bit = 0
    b = []
    while n > 0:
        c = n%2
        b.append(c)
        bit += 1
        n = n//2
    b.reverse()
    return b, bit

print(conv_bin(10))
