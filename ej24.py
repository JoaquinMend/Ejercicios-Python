a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x1 = (-b + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
x2 = (-b - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)

print("")
print("x1: " + str(x1))
print("x2: " + str(x2))
