from collections import deque
import re

def solve(input):
	size = 71
	map = [["."] * size for _ in range(size)]

	for line in input.splitlines()[:1024]:
		for (a, b) in re.findall(r"(\d+),(\d+)", line):
			map[int(b)][int(a)] = "#"

	gx = size - 1
	gy = size - 1

	visited = set()
	q = deque()
	q.append((0, 0, 0))

	while len(q) > 0:
		(d, i, j) = q.popleft()
		if i < 0 or i >= size or j < 0 or j >= size: continue
		if map[i][j] == "#": continue
		if (i, j) in visited: continue
		visited.add((i, j))

		if i == gx and j == gy: return d

		q.append((d + 1, i - 1, j))
		q.append((d + 1, i + 1, j))
		q.append((d + 1, i, j - 1))
		q.append((d + 1, i, j + 1))
