n = int(input("Ingrese un número de 5 dígitos: "))

c_1 = int(n / 10)
r_1 = int(n % 10)

c_2 = int(c_1 / 10)
r_2 = int(c_1 % 10)

c_3 = int(c_2 / 10)
r_3 = int(c_2 % 10)

c_4 = int(c_3 / 10)
r_4 = int(c_3 % 10)

rf = int((r_1 * 10000) + (r_2 * 1000) + (r_3 * 100) + (r_4 * 10) + c_4)

print("")
print("Inverso: " + str(rf))
