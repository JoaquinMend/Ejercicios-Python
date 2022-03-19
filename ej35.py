m = int(input("Mes: "))
a = int(input("Año: "))
if m == 1:
	print("Mes: ENERO")
	print("Días: 31")
elif m == 2:
	if a % 4 == 0 and a % 100 != 0:
		print("Mes: FEBRERO")
		print("Días: 29")
	else:
		print("Mes: FEBRERO")
		print("Días: 28")
elif m == 3:
	print("Mes: MARZO")
	print("Días: 31")
elif m == 4:
	print("Mes: ABRIL")
	print("Días: 30")
elif m == 5:
	print("Mes: MAYO")
	print("Días: 31")
elif m == 6:
	print("Mes: JUNIO")
	print("Días: 30")
elif m == 7:
	print("Mes: JULIO")
	print("Días: 31")
elif m == 8:
	print("Mes: AGOSTO")
	print("Días: 31")
elif m == 9:
	print("Mes: SEPTIEMBRE")
	print("Días: 30")
elif m == 10:
	print("Mes: OCTUBRE")
	print("Días: 31")
elif m == 11:
	print("Mes: NOVIEMBRE")
	print("Días: 30")
elif m == 12:
	print("Mes: DICIEMBRE")
	print("Días: 31")
else:
	print("MES NO VÁLIDO")
