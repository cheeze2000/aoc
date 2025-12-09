def solve(input):
	grid = input.splitlines()
	r = len(grid)
	c = len(grid[0])

	def get(i, j):
		if 0 <= i < r and 0 <= j < c:
			return grid[i][j]

	def neighbour_count(i, j):
		ans = 0

		for di in [-1, 0, 1]:
			for dj in [-1, 0, 1]:
				if di == 0 and dj == 0:
					continue

				if get(i + di, j + dj) == "@":
					ans += 1

		return ans

	ans = 0

	for i in range(r):
		for j in range(c):
			if get(i, j) == "@" and neighbour_count(i, j) < 4:
				ans += 1

	return ans
