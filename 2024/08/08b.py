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
				extend(locations[i], locations[j], visited, (r, c))

	return len(visited)

def extend(symbol1, symbol2, visited, bounds):
	r, c = bounds
	x1, y1 = symbol1
	x2, y2 = symbol2

	dx = x2 - x1
	dy = y2 - y1

	x3 = x2 + dx
	y3 = y2 + dy
	while 0 <= x3 < r and 0 <= y3 < c:
		visited.add((x3, y3))
		x3 += dx
		y3 += dy

	x3 = x1 - dx
	y3 = y1 - dy
	while 0 <= x3 < r and 0 <= y3 < c:
		visited.add((x3, y3))
		x3 -= dx
		y3 -= dy

	visited.add(symbol1)
	visited.add(symbol2)
