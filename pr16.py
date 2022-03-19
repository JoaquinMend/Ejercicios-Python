n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))
n4 = int(input("Nota 4: "))
if n1 < n2 and n1 < n3 and n1 < n4:
	suma = (n2 + n3 + n4)
	promedio = suma/2
elif n2 < n1  and n2 < n3 and n2 < n4:
	suma = (n1 + n3 + n4)
	promedio = suma/2
elif n3 < n1 and n3 < n2 and n3 < n4:
	suma = (n2 + n1 + n4)
	promedio = suma/2
else:
	suma = (n2 + n3 + n1)
	promedio = suma/2
if promedio >= 11:
	print("")
	print("Estado: Aprobado")
else:
	print("")
	print("Estado: Desaprobado")
	
