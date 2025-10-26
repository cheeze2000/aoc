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

	start = (i, j)
	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	k = 0

	path = set()

	while True:
		ii = i + dirs[k][0]
		jj = j + dirs[k][1]

		if get(i, j) == "": break

		if get(ii, jj) == "#":
			k = (k + 1) % 4
			continue

		path.add((i, j))
		i = ii
		j = jj

	ans = 0

	path.remove(start)
	for i, j in path:
		if is_looping(map, start, (i, j)): ans += 1

	return ans

def is_looping(map, start, obj):
	states = set()
	i, j = start
	map[obj[0]][obj[1]] = "#"

	r = len(map)
	c = len(map[0])

	def get(i, j):
		if 0 <= i < r and 0 <= j < c: return map[i][j]
		return ""

	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	k = 0

	while True:
		if (i, j, k) in states:
			ans = True
			break
		states.add((i, j, k))

		ii = i + dirs[k][0]
		jj = j + dirs[k][1]

		if get(i, j) == "":
			ans = False
			break

		if get(ii, jj) == "#":
			k = (k + 1) % 4
			continue

		i = ii
		j = jj

	map[obj[0]][obj[1]] = "."

	return ans
