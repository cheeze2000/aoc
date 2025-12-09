from functools import cache

def solve(input):
	grid = input.splitlines()
	r = len(grid)
	c = len(grid[0])

	ans = 0

	@cache
	def beam(i, j):
		nonlocal ans

		if i < 0 or j < 0 or i >= r or j >= c:
			return

		if grid[i][j] == "^":
			ans += 1
			beam(i, j - 1)
			beam(i, j + 1)
		else:
			beam(i + 1, j)

	for i in range(r):
		for j in range(c):
			if grid[i][j] == "S":
				beam(i, j)

	return ans
