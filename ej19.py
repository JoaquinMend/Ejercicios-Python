c = int(input("Consumo: "))
if c < 101:
	m_d = c * 0.1
	m_igv = (c - m_d) * 0.19
	m_r = c - m_d + m_igv
	print("")
	print("Monto descuento: " + str(m_d))
	print("Impuesto IGV: " + str(m_igv))
	print("Importe a pagar: " + str(m_r))
else:
	m_d = c * 0.2
	m_igv = (c - m_d) * 0.19
	m_r = c - m_d + m_igv
	print("")
	print("Monto descuento: " + str(m_d))
	print("Impuesto IGV: " + str(m_igv))
	print("Importe a pagar: " + str(m_r))
