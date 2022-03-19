m_c = int(input("Monto de compra: "))
t_cl = input("Tipo de cliente: ")
f_p = input("Forma de pago: ")
if t_cl == "G":
	if f_p == "C":
		d_r = m_c * 0.15
		c_r = m_c - d_r
		print("")
		print("Descuento 15%: " + str(d_r))
		print("Total a pagar: " + str(c_r))
	elif f_p == "P":
		d_r = m_c * 0.10
		c_r = m_c + d_r
		print("")
		print("Recargo 10%: " + str(d_r))
		print("Total a pagar: " + str(c_r))
	else:
		print("")
		print("FORMA DE PAGO NO VALIDA (SOLO 'C' O 'P')")
elif t_cl == "A":
	if f_p == "C":
		d_r = m_c * 0.20
		c_r = m_c - d_r
		print("")
		print("Descuento 20%: " + str(d_r))
		print("Total a pagar: " + str(c_r))
	elif f_p == "P":
		d_r = m_c * 0.05
		c_r = m_c + d_r
		print("")
		print("Recargo 5%: " + str(d_r))
		print("Total a pagar: " + str(c_r))
	else:
		print("")
		print("FORMA DE PAGO NO VALIDA (SOLO 'C' O 'P')")
else:
	print("TIPO DE CLIENTE NO VALIDO (SOLO 'G' O 'A')")
