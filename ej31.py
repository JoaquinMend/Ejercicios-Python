n = int(input("Promedio: "))
if n >= 0 and n < 6:
	print("PÉSIMO")
elif n > 5 and n < 11:
	print("MALO")
elif n > 10 and n < 15:
	print("REGULAR")
elif n > 14 and n < 18:
	print("BUENO")
elif n > 17 and n < 21:
	print("EXCELENTE")
else:
	print("PROMEDIO NO VÁLIDO (SOLO ENTRE 0 Y 20)")
