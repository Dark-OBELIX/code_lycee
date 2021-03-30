def multiplication(n1, n2):
    if n2 >= 0 or n1 >= 0:
        res = 0
        for i in range(0, n1):
            res = res + n2
        print(res)

    else:
        res = 0
        for i in range(n1, 0):
            res = res - n2
        print(res)

multiplication(-2, -5)
