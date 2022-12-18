from random import random as rand
# X
# х1 – менеджер; 
# х2 – програміст; 
# х3 – водій; 
# х4 – секретар. 
# Y
# у1 – гнучкість мислення; 
# у2 – уміння швидко приймати рішення; 
# у3 – концентрація уваги; 
# у4 – зорова пам’ять; 
# у5 – витривалість; 
# у6 – швидкість реакції рухів; 
# у7 – відповідальність. - 
# Z
# z1 – Андрієнко; 
# z2 – Василенко; 
# z3 – Іваненко; 
# z4 – Дмитренко; 
# z5 – Петренко; 
# z6 – Романенко. 
from typing import List


def printMarrix(matrix: List[List[float]], column_label: List[str], row_label: List[str]) -> None:
	print(column_label)
	for i in range(0, len(matrix)):
		print(row_label[i], matrix[i])


def alternative_composition(matrix1: List[List[float]], matrix2: List[List[float]]):
	answer: List[List[float]] = []
	for i in range(0, len(matrix1)):
		answer.append([])
		for j in range(0, len(matrix2[0])):
			temp: List[float] = []
			for k in range(0, len(matrix1[0])):
				temp.append(matrix1[i][k] * matrix2[k][j])
				# answer[i].append(max(temp))
			answer[i].append(float(format(max(temp), '.2f')))
	return answer


def composition(matrix1: List[List[float]], matrix2: List[List[float]]):
	answer: List[List[float]] = []
	for i in range(0, len(matrix1)):
		answer.append([])
		for j in range(0, len(matrix2[0])):
			temp: List[float] = []
			for k in range(0, len(matrix1[0])):
				temp.append(min(matrix1[i][k], matrix2[k][j]))
				# answer[i].append(max(temp))
			answer[i].append(float(format(max(temp), '.2f')))
	return answer


def main() -> int:
	x_labels: List[str] = ['x1', 'x2', 'x3', 'x4']
	y_labels: List[str] = ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7']
	z_labels: List[str] = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6']
	# y1 y2 y3 y4 y5 y6 y7
	S: List[List[float]] = [[0.55, 1.00, 0.70, 0.40, 0.25, 0.10, 0.85],  # х1
                            [1.00, 0.55, 0.85, 0.40, 0.25, 0.10, 0.70],  # х2
                            [0.50, 0.85, 0.50, 0.55, 0.70, 1.00, 0.40],  # x3
                            [0.40, 0.70, 0.85, 0.55, 0.60, 0.10, 1.00]]  # x4
	# # z1 z2 z3 z4 z5 z6
	# Q: list[list[float]] = [[0.00, 0.00, 0.00, 0.00, 0.00, 0.00], #y1
	# [0.00, 0.00, 0.00, 0.00, 0.00, 0.00], #y2
	# [0.00, 0.00, 0.00, 0.00, 0.00, 0.00], #y3
	# [0.00, 0.00, 0.00, 0.00, 0.00, 0.00], #y4
	# [0.00, 0.00, 0.00, 0.00, 0.00, 0.00], #y5
	# [0.00, 0.00, 0.00, 0.00, 0.00, 0.00], #y6
	# [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]] #y7
	Q: List[List[float]] = [[float(format(rand(), '.2f')) for i in range(0, 6)]
	                        for j in range(0, 7)]
	print("S")
	printMarrix(S, y_labels, x_labels)
	print("Q")
	printMarrix(Q, z_labels, y_labels)
	print("Composition")
	printMarrix(composition(S, Q), z_labels, x_labels)
	print("Alternative Composition")
	printMarrix(alternative_composition(S, Q), z_labels, x_labels)
	composition(S, Q)
	# printMarrix(S, z_labels, x_labels)
	return 0


if __name__ == '__main__':
	main()