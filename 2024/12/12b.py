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
	edges = set()

	for (i, j) in region:
		if (i - 1, j) not in cells:
			edges.add((i, j, 2))
		if (i + 1, j) not in cells:
			edges.add((i, j, 1))
		if (i, j - 1) not in cells:
			edges.add((i, j, 0))
		if (i, j + 1) not in cells:
			edges.add((i, j, 3))

	lefts = segments(edges, 0)
	downs = segments(edges, 1)
	ups = segments(edges, 2)
	rights = segments(edges, 3)

	return lefts + downs + ups + rights

def segments(edges, dir):
	is_vertical = dir == 0 or dir == 3
	sort_key = (lambda x: (x[1], x[0])) if is_vertical else (lambda x: (x[0], x[1]))
	edges = sorted([edge for edge in edges if edge[2] == dir], key=sort_key)
	edge_set = set(edges)

	ans = 0
	for (i, j, d) in edges:
		if (i, j, d) not in edge_set: continue

		a = i
		b = j
		while (a, b, d) in edge_set:
			edge_set.remove((a, b, d))
			if is_vertical:
				a += 1
			else:
				b += 1

		ans += 1

	return ans
