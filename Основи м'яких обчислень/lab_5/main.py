from typing import List


def printMatrix(matrix: List[List[float]]) -> None:
	for row in matrix:
		print(row)


def composition(matrix1: List[List[float]], matrix2: List[List[float]]):
	answer: List[List[float]] = []
	size = len(matrix1)
	for i in range(0, size):
		answer.append([])
		for j in range(0, size):
			temp: List[float] = []
			for k in range(0, size):
				temp.append(min(matrix1[i][k], matrix2[k][j]))
			answer[i].append(float(format(max(temp), '.2f')))
	return answer


def tranzit_lock(matrix: List[List[float]]):
	prev_matrix: List[List[float]] = [[]]
	current_matrix: List[List[float]] = [[]]
	prev_matrix = matrix
	n = 2
	while 1:
		current_matrix = composition(matrix, prev_matrix)
		if current_matrix == prev_matrix:
			break
		prev_matrix = current_matrix
		print(f'n = {n}')
		printMatrix(prev_matrix)
		n += 1


def main() -> int:
	Q: List[List[float]] = [[1.0, 0.0, 0.6, 0.0, 0.0, 0.0],
	                        [0.0, 1.0, 0.5, 0.4, 0.7, 0.0],
	                        [0.7, 0.6, 1.0, 0.0, 0.5, 0.0],
	                        [0.0, 0.5, 0.0, 1.0, 0.0, 0.6],
	                        [0.0, 0.3, 0.4, 0.0, 1.0, 0.1],
	                        [0.0, 0.0, 0.0, 0.6, 0.3, 1.0]]
	# Q: list[list[float]] = [[1.0, 0.0, 1.0, 0.0, 0.0, 0.0],
	# [0.0, 1.0, 1.0, 1.0, 1.0, 0.0],
	# [1.0, 1.0, 1.0, 0.0, 1.0, 0.0],
	# [0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
	# [0.0, 1.0, 1.0, 0.0, 1.0, 1.0],
	# [0.0, 0.0, 0.0, 1.0, 1.0, 1.0]]
	print('Q')
	printMatrix(Q)
	tranzit_lock(Q)
	return 0


if __name__ == '__main__':
	main() 