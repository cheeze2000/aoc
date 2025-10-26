from collections import deque
import re

def solve(input):
	size = 71
	map = [["."] * size for _ in range(size)]
	obstacles = []

	for line in input.splitlines():
		for (a, b) in re.findall(r"(\d+),(\d+)", line):
			map[int(b)][int(a)] = "#"
			obstacles.append((int(b), int(a)))

	disj = dict()

	def parent(a):
		if a not in disj:
			disj[a] = a
		if disj[a] == a: return a
		disj[a] = parent(disj[a])
		return disj[a]

	def unify(a, b):
		pa = parent(a)
		pb = parent(b)
		disj[pa] = pb

	for i in range(size):
		for j in range(size):
			if map[i][j] == "#": continue
			i1 = i + 1
			j1 = j
			i2 = i
			j2 = j + 1

			if i1 < size and map[i1][j1] == ".":
				unify((i, j), (i1, j1))
			if j2 < size and map[i2][j2] == ".":
				unify((i, j), (i2, j2))

	while True:
		(i, j) = obstacles.pop()
		map[i][j] = "."

		if i - 1 >= 0 and map[i - 1][j] == ".":
			unify((i, j), (i - 1, j))
		if i + 1 < size and map[i + 1][j] == ".":
			unify((i, j), (i + 1, j))
		if j - 1 >= 0 and map[i][j - 1] == ".":
			unify((i, j), (i, j - 1))
		if j + 1 < size and map[i][j + 1] == ".":
			unify((i, j), (i, j + 1))

		if parent((0, 0)) == parent((size - 1, size - 1)):
			return f"{j},{i}"
