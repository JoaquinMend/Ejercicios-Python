n = int(input("Puntaje: "))
if n > 69 and n < 80:
	print("Administración")
elif n > 79 and n < 90:
	print("Industrial")
elif n > 89 and n < 100:
	print("Electrónica")
elif n >= 100:
	print("Sistemas")
else:
	print("NO INGRESÓ")
