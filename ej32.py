dia = int(input("Día(entre 1 y 31): "))
mes = int(input("Mes(entre 1 y 12): "))
Verano = [1,2,3]
Otoño = [4,5,6]
Invierno = [7,8,9]
Primavera = [10,11,12]
if dia > 31:
	e = "DIA O MES NO VÁLIDOS"
elif mes in Verano:
	e = "VERANO"
	if mes == 3 and dia > 20:
		e = "OTOÑO"
elif mes in Otoño:
	e = "OTOÑO"
	if mes == 6 and dia > 21:
		e = "INVIERNO"
elif mes in Invierno:
	e = "INVIERNO"
	if mes == 9 and dia > 22:
		e = "PRIMAVERA"
elif mes in Primavera:
	e = "PRIMAVERA"
	if mes == 12 and dia > 20:
		e = "VERANO"
else:
	e = "DÍA O MES NO VÁLIDOS"
	
print("Estación: " + e)
