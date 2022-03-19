c = input("Colegio: ")
n = input("Nivel: ")
if c == "N":
	if n == "A":
		print("Monto a pagar: 300")
	elif n == "B":
		print("Monto a pagar: 200")		
	elif n == "C":
		print("Monto a pagar: 100")
	else:
		print("NIVEL NO VÁLIDO (SOLO A, B, C)")
elif c == "P":
	if n == "A":
		print("Monto a pagar: 400")
	elif n == "B":
		print("Monto a pagar: 300")		
	elif n == "C":
		print("Monto a pagar: 200")
	else:
		print("NIVEL NO VÁLIDO (SOLO A, B, C)")
else:
	print("COLEGIO NO VÁLIDO (SOLO N O P)")
