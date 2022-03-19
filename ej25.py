h = int(input("Hora: "))
m = int(input("Minuto: "))
s = int(input("Segundo: "))

s = s+1

if s == 60:
	s = 0
	m = m + 1
	if m == 60:
		m = 0
		h = h + 1
		if h == 24:
			h = 0
print("")
print("Hora: " + str(h))
print("Minuto: " + str(m))
print("Segundo: " + str(s))
