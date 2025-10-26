def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	def get(i, j):
		if 0 <= i < r and 0 <= j < c: return map[i][j]
		return ""

	i = 0
	j = 0

	for a in range(r):
		for b in range(c):
			if map[a][b] == "^":
				i = a
				j = b

	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	k = 0

	ans = 0
	while True:
		ii = i + dirs[k][0]
		jj = j + dirs[k][1]

		if get(i, j) == "": return ans

		if get(ii, jj) == "#":
			k = (k + 1) % 4
			continue

		if get(i, j) != "X":
			map[i][j] = "X"
			ans += 1

		i = ii
		j = jj
