from functools import cache

def solve(input):
	grid = input.splitlines()
	r = len(grid)
	c = len(grid[0])

	@cache
	def beam(i, j):
		if i < 0 or j < 0 or i >= r or j >= c:
			return 1

		if grid[i][j] == "^":
			return beam(i, j - 1) + beam(i, j + 1)
		else:
			return beam(i + 1, j)

	for i in range(r):
		for j in range(c):
			if grid[i][j] == "S":
				return beam(i, j)
