def f(x):
	return x**3 - 3*x + 1

def algo_dicho(a,b,n):

	while (b - a) > 10**-n:
		m =(a + b) / 2

		if (f(a) * f(m)) < 0:
			b = m

		else :
			a = m

	return m,a,b

############################################################

print(algo_dicho(-1,1,4))

#Quand n = 1:
#	a = 0.3125
#	b = 0.375
# 	m = 0.3125

#Quand n = 4:
#	a = 0.3472900390625
#   b = 0.34735107421875
#   m = 0.34735107421875