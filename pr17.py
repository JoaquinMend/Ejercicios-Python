s_a = int(input("Saldo anterior: "))
t_m = input("Tipo de movimiento: ")
m_t = int(input("Monto de transacción: "))
if t_m == "R":
	s_r = s_a - m_t
	print("")
	print("Saldo actual: " + str(s_r))
elif t_m == "D":
	s_r = s_a + m_t
	print("")
	print("Saldo actual: " + str(s_r))
else:
	print("TIPO DE MOVIMIENTO NO VALIDO (SOLO 'R' O 'D')")
