from matplotlib import pyplot as plt


def aproc(x: int, a: int, b: int, c: int, d: int) -> float:
    if x < a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)
    else:
        return 0


def carrier(array_label: list[int], array_mu: list[float]):
    temp: list[int] = []
    for i in range(0, len(array_mu)):
        if array_mu[i]:
            temp.append(array_label[i])
    print("Носій")
    print(temp)


def core(array_label: list[int], array_mu: list[float]):
    temp: list[int] = []
    for i in range(0, len(array_mu)):
        if array_mu[i] == 1:
            temp.append(array_label[i])
    print("Ядро")
    print(temp)


def border(array_label: list[int], array_mu: list[float]):
    temp: list[int] = []
    for i in range(0, len(array_mu)):
        if 0 < array_mu[i] < 1.0:
            temp.append(array_label[i])
    print("Межі")
    print(temp)


a: int = 160
b: int = 170
c: int = 180
d: int = 190
array_label: list[int] = [x for x in range(150, 205, 5)]
array_mu: list[float] = []
array_mu_aprox: list[float] = []
matrix: list[list[float]] = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
]
size_i: int = len(matrix)
size_j: int = len(matrix[0])
for j in range(0, size_j):
    sup: float = 0
    mu: float = 0
    for i in range(0, size_i):
        mu += matrix[i][j]
    if sup < matrix[i][j]:
        sup = matrix[i][j]
    if sup:
        mu /= sup * size_i
    array_mu.append(mu)


for x in array_label:
    array_mu_aprox.append(aproc(x, a, b, c, d))
carrier(array_label, array_mu_aprox)
core(array_label, array_mu_aprox)
border(array_label, array_mu_aprox)
temp = []
array_mu_max = max(array_mu)
for i in array_mu:
    temp.append(i / array_mu_max)
plt.plot(array_label, temp, label='Експерти')
plt.legend(loc=2)
plt.show()
plt.plot(array_label, array_mu_aprox, label='Апроксимація')
plt.legend(loc=2)
plt.show()
