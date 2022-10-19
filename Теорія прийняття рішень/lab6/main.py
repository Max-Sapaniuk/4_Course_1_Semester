import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path_1 = "matrix1.txt"
rel_path_2 = "matrix2.txt"
path_to_file_1 = os.path.join(script_dir, rel_path_1)
path_to_file_2 = os.path.join(script_dir, rel_path_2)


def transpose_marix(matr1):
	length1 = len(matr1)
	matr = [[0 for k in range(len(matr1[0]))] for n in range(length1)]
	for n in range(length1):
		for k in range(len(matr1[0])):
			matr[k][n] = matr1[n][k]
	return matr


def find_reverse(matr):
	length = len(matr)
	RES = [[0 for k in range(len(matr[0]))] for n in range(length)]
	for n in range(length):
		for k in range(len(matr[0])):
			RES[n][k] = True if matr[n][k] == False else False
	return RES


def find_max(matr):
	majorants = []
	for e in matr:
		majorants.append(sum(e))
	mx = max(majorants)
	return majorants, mx


def find_min(matr):
	matr = transpose_marix(matr)
	majorants = []
	for e in matr:
		majorants.append(sum(e))
	mx = max(majorants)
	return majorants, mx


def find_majorants(matr):
	matr = transpose_marix(find_reverse(matr))
	majorants = []
	for e in matr:
		majorants.append(sum(e))
	return majorants, max(majorants)


def find_minorants(matr):
	matr = find_reverse(matr)
	minorants = []
	for e in matr:
		minorants.append(sum(e))
	mx = max(minorants)
	return minorants, mx


def print_out_matrix(matr):
	for e in matr:
		for e2 in e:
			print(e2 * 1, end=" ")
		print()


def intersecion(A, B):
	lenght = len(A)
	RES = [[0 for k in range(len(A[0]))] for n in range(lenght)]
	for n in range(lenght):
		for k in range(len(A[0])):
			RES[n][k] = A[n][k] & B[n][k]
	return RES


def union(A, B):
	lenght = len(A)
	RES = [[0 for k in range(len(A[0]))] for n in range(lenght)]
	for n in range(lenght):
		for k in range(len(A[0])):
			RES[n][k] = B[n][k] or A[n][k]
	return RES


def tolerance(matrix):
	return intersecion(matrix, transpose_marix(matrix))


def incomparability(matrD, matrB):
	temp1 = union(matrD, matrB)
	temp2 = union(temp1, transpose_marix(matrD))
	return temp2


def difference(A, B):
	length = len(A)
	RES = [[0 for k in range(len(A[0]))] for n in range(length)]
	for n in range(length):
		for k in range(len(A[0])):
			RES[n][k] = A[n][k] & (1 if B[n][k] == 0 else 0)
	return RES

# 1
print("Завдання №4")
with open(path_to_file_1, 'r') as file:
	matr = [list(map(lambda x: True if x == '1' else False, line.replace("\n", '').split())) for line in
	        file.readlines()]
print("Вхідна матриця:")
print_out_matrix(matr)
print("\nБайдужості:")
tol = tolerance(matr)
print_out_matrix(tol)
print("\nДомінування:")
diff = difference(matr, tol)
print_out_matrix(diff)
print("\nНепорівняності:")
inc = incomparability(diff, tol)
print_out_matrix(inc)

# 2
print("\nЗавдання №5")
with open(path_to_file_2, 'r') as file:
	matr = [list(map(lambda x: True if x == '1' else False, line.replace("\n", '').split())) for line in
	        file.readlines()]
print("Вхідна матриця:")
print_out_matrix(matr)
print()
majorants, mx = find_majorants(matr)
print("Мажоранти:")
for i in range(len(majorants)):
	if majorants[i] == mx:
		print("x" + str(i + 1), end=", ")
print("\n")
minorants, mx2 = find_minorants(matr)
print("Міноранти:")
for i in range(len(minorants)):
	if (minorants[i] == mx2):
		print("x" + str(i + 1), end=", ")
print("\n")
print("Максимум: ")
majorants, mx = find_max(matr)
for i in range(len(minorants)):
	if (majorants[i] == mx):
		print("x" + str(i + 1), end=", ")
print("\n")
print("Мінімум: ")
minorants, mx2 = find_min(matr)
for i in range(len(minorants)):
	if (minorants[i] == mx2):
		print("x" + str(i + 1), end=", ")
print("\n")
