def fibonacci(n):
    u1 = 1
    u2 = 1
    if n <= 2:
        return 1
    elif n >= 3:
        terme_prec = u1
        terme = u2
        terme_nxt = u1 + u2
        total = 0
        for i in range(1, n-2):
            total = terme + terme_nxt
            terme = terme_nxt 
            terme_nxt = total
        
        return total
    else:
        print("Une erreur est survenue...")

print(fibonacci(25))
