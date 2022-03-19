op = input("Ingrese el operador (+, -, *, /): ")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
if op == "+":
	r = n1 + n2
	print("Resultado: " + str(r))
elif op == "-":
	r = n1 - n2
	print("Resultado: " + str(r))
elif op == "*":
	r = n1 * n2
	print("Resultado: " + str(r))
elif op == "/":
	if n2 == 0:
		print("Resultado: 0")
	else:
		r = n1 / n2
		print("Resultado: " + str(r))
else:
	print("OPERADOR NO VÁLIDO")
