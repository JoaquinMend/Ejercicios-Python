lado_1 = int(input("Longitud 1: "))
lado_2 = int(input("Longitud 2: "))
lado_3 = int(input("Longitud 3: "))
if lado_1 < (lado_2 + lado_3) and lado_1 > (lado_2 - lado_3):
	if lado_2 < (lado_1 + lado_3) and lado_2 > (lado_1 - lado_3):
		if lado_3 < (lado_2 + lado_1) and lado_3 > (lado_2 - lado_1):
			print("SÍ ES TRIÁNGULO")
else:
	print("NO ES TRIANGULO")
