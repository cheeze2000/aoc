def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	ans = 0

	for i in range(r):
		for j in range(c):
			if map[i][j] != "X": continue

			for a in range(-1, 2):
				for b in range(-1, 2):
					if a == 0 and b == 0: continue
					ans += is_xmas(map, (a, b), i, j)

	return ans

def is_xmas(map, direction, x, y):
	def get(i, j):
		if 0 <= i < len(map) and 0 <= j < len(map[0]):
			return map[i][j]
		return ""

	dx, dy = direction
	mas = get(x + dx, y + dy) + get(x + 2 * dx, y + 2 * dy) + get(x + 3 * dx, y + 3 * dy)

	if mas == "MAS":
		return 1

	return 0
