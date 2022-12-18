print("Трикутні нечіткі числа")
print("A")
a = float(input("a= "))
alfa = float(input("alfa= "))
beta = float(input("beta= "))
print("B")
a2 = float(input("a= "))
alfa2 = float(input("alfa= "))
beta2 = float(input("beta= "))
print("C")
a3 = float(input("a= "))
alfa3 = float(input("alfa= "))
beta3 = float(input("beta= "))
print()
print("A+(C/T*A)-B")
# print("(A/B)+(C*B)-B")
c2 = a2 * a3
b2 = a2 * alfa3 + a3 * alfa2
d2 = a2 * beta3 + alfa3 * beta2
print("C*B->\n", c2, b2, d2)
c3 = a / a2
b3 = (a * beta2 + a2 * alfa) / pow(a2, 2)
d3 = (a * alfa2 + a2 * beta) / pow(a2, 2)
print("A/B->\n", c3, b3, d3)
c1 = c2 - a2
b1 = b2 + beta2
d1 = alfa2 + d2
c4 = c3 + c1
b4 = b3 + b1
d4 = d3 + d1
print("(A/B)+(C*B)-B\n", c4, b4, d4)
