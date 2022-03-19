a = int(input("Número 1: "))
b = int(input("Número 2: "))
if a > b:
	n = a - b - 1
	print("")
	print("Hay " + str(n) + " números entre el Número 1 y el Número 2.")
else:
	n = b - a - 1
	print("")
	print("Hay " + str(n) + " números entre el Número 1 y el Número 2.")
