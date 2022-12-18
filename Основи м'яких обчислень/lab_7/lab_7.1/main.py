print("Трикутні нечіткі числа")
print("A")
a = float(input("a= "))
alfa = float(input("alfa= "))
beta = float(input("beta= "))
print("B")
a2 = float(input("a= "))
alfa2 = float(input("alfa= "))
beta2 = float(input("beta= "))
print()
print("Трапецеподібні нечіткі інтервал")
print("A")
a_ = float(input("a1= "))
b1 = float(input("b1= "))
alfa_ = float(input("alfa= "))
beta_ = float(input("beta= "))
print("B")
a2_ = float(input("a2= "))
b2 = float(input("b2= "))
alfa2_ = float(input("alfa2= "))
beta2_ = float(input("beta2= "))
c = a + a2
b = alfa + alfa2
d = beta + beta2
print("Операції трикутні нечіткі числа")
print("Додавання\n", c, b, d)
c1 = a - a2
b1 = alfa + beta2
d1 = alfa2 + beta
print("Віднімання\n", c1, b1, d1)
c2 = a * a2
b2 = a * alfa2 + a2 * alfa
d2 = a * beta2 + alfa2 * beta
print("Множення\n", c2, b2, d2)
c3 = a / a2
b3 = (a * beta2 + a2 * alfa) / pow(a2, 2)
d3 = (a * alfa2 + a2 * beta) / pow(a2, 2)
print("Ділення\n", c3, b3, d3)
print()
c4 = a_ + a2_
x4 = b1 + b2
b4 = alfa_ + alfa2_
d4 = beta_ + beta2_
print("Трапецеподібні нечіткі інтервал")
print("Додавання\n", c4, x4, b4, d4)
c5 = a_ - a2_
x5 = b1 - b2
b5 = alfa_ + beta2_
d5 = alfa2_ + beta_
print("Віднімання\n", c5, x5, b5, d5)
c6 = a_ * a2_
x6 = b1 * b2
b6 = a_ * alfa2_ + a2_ * alfa_
d6 = b1 * beta2_ + b2 * beta_
print("Множення\n", c6, x6, b6, d6)
c7 = a_ / b2
x7 = b1 / a2_
b7 = (a_ * beta2_ + b2 * alfa_) / pow(b2, 2)
d7 = (b1 * alfa_ + a2_ * beta_) / pow(a2_, 2)
print("Ділення\n", c7, x7, b7, d7)
