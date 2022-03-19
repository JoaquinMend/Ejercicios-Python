temp = int(input("Temperatura: "))
if temp < 10:
	print("Clima: FRÍO")
elif temp >= 10 and temp <= 20:
	print("Clima: NUBLADO")
elif temp >= 21 and temp <= 30:
	print("Clima: CALOR")
else:
	print("Clima: TROPICAL") 
