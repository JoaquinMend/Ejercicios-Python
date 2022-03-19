n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
if n1 > n2 and n1 > n3:
	mayor = n1
else:
	if n2 > n1 and n2 > n3:
		mayor = n2
	else:
		mayor = n3
if n1 < n2 and n1 < n3:
	menor = n1
else:
	if n2 < n1 and n2 < n3:
		menor = n2
	else:
		menor = n3
medio = (n1+n2+n3) - (mayor + menor)

print("")
print("Orden ascendente: " + str(menor) + ", " + str(medio) + ", " + str(mayor))
print("Orden descendente: " + str(mayor) + ", " + str(medio) + ", " + str(menor))
