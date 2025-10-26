from collections import defaultdict

def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	symbols = defaultdict(list)
	visited = set()

	for i in range(r):
		for j in range(c):
			symbol = map[i][j]
			if symbol != ".":
				symbols[symbol].append((i, j))

	for locations in symbols.values():
		n = len(locations)

		for i in range(n - 1):
			for j in range(i + 1, n):
				extend(locations[i], locations[j], visited)

	return len([(a, b) for (a, b) in visited if 0 <= a < r and 0 <= b < c])

def extend(symbol1, symbol2, visited):
	x1, y1 = symbol1
	x2, y2 = symbol2

	dx = x2 - x1
	dy = y2 - y1

	visited.add((x2 + dx, y2 + dy))
	visited.add((x1 - dx, y1 - dy))
