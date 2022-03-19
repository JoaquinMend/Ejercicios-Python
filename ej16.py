n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
if n1 > n2:
	if n1 > n3:
		print("Mayor: " + str(n1))
	else:
		print("Mayor: " + str(n3))
else:
	if n2 > n3:
		print("Mayor: " + str(n2))
	else:
		print("Mayor: " + str(n3))
