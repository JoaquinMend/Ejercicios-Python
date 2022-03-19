c = int(input("Capital: "))
ti = int(input("Tasa de interés: "))
t = int(input("Tiempo: "))

m = float(((1+ti/100)**t)*c)
i = m - c

print("")
print("Interés: " + str(i))
print("Monto: " + str(m))
