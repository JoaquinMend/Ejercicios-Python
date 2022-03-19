n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
n4 = int(input("Número 4: "))

s = int(n1+n2+n3+n4)

p1 = (n1*100)/s
p2 = (n2*100)/s
p3 = (n3*100)/s
p4 = (n4*100)/s
print("")
print("Suma: " + str(s))
print("Porcentaje 1: " + str(p1) + "%")
print("Porcentaje 2: " + str(p2) + "%")
print("Porcentaje 3: " + str(p3) + "%")
print("Porcentaje 4: " + str(p4) + "%")
