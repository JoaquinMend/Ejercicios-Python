c = int(input("Calidad: "))
p = int(input("Producto: "))
if p == 1:
	if c == 1:
		print("Precio: 5000")
	elif c == 2:
		print("Precio: 4500")
	elif c == 3:
		print("Precio: 4000")
	else:
		print("CALIDAD NO VÁLIDA")
elif p == 2:
	if c == 1:
		print("Precio: 4500")
	elif c == 2:
		print("Precio: 4000")
	elif c == 3:
		print("Precio: 3500")
	else:
		print("CALIDAD NO VÁLIDA")
elif p == 3:
	if c == 1:
		print("Precio: 4000")
	elif c == 2:
		print("Precio: 3500")
	elif c == 3:
		print("Precio: 3000")
	else:
		print("CALIDAD NO VÁLIDA")
else:
	print("PRODUCTO NO VÁLIDO")
