n = int(input("Mes: "))
Verano = [1, 2, 3]
Invierno = [7, 8, 9]
Otoño = [4, 5, 6]
Primavera = [10, 11, 12]
if n in Verano:
	print("VERANO")
elif n in Otoño:
	print("OTOÑO")
elif n in Invierno:
	print("INVIERNO")
elif n in Primavera:
	print("PRIMAVERA")
else:
	print("MES NO VÁLIDO (ENTRE 1 Y 12)")
