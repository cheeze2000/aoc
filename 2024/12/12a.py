def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	visited = set()
	regions = []

	region = []
	def dfs(i, j, plant):
		if i < 0 or i >= r or j < 0 or j >= c: return
		if map[i][j] != plant: return
		if (i, j) in visited: return
		visited.add((i, j))
		region.append((i, j))
		dfs(i - 1, j, plant)
		dfs(i + 1, j, plant)
		dfs(i, j - 1, plant)
		dfs(i, j + 1, plant)

	for i in range(r):
		for j in range(c):
			if (i, j) in visited: continue
			region = []
			dfs(i, j, map[i][j])
			regions.append(region)

	cost = sum(perimeter(region) * len(region) for region in regions)

	return cost

def perimeter(region):
	cells = set(region)

	value = 4 * len(region)
	for (i, j) in region:
		if (i - 1, j) in cells: value -= 1
		if (i + 1, j) in cells: value -= 1
		if (i, j - 1) in cells: value -= 1
		if (i, j + 1) in cells: value -= 1

	return value
