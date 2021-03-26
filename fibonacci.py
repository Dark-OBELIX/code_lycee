def fibonacci(valeur):
	
    var_last = 1
    var_last_2 = 1
    var_temp = 0
    i=0

    while i <= valeur:
        if i > 2:
            var_temp = var_last + var_last_2
            var_last_2 = var_last
            var_last = var_temp
        else:
            var_temp = 1
        i = i + 1

    return var_temp

############################################################

print(fibonacci(7))

# 13
