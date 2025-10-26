def solve(input):
	[i1, i2] = input.split("\n\n")
	map = [list(line) for line in i1.splitlines()]
	path = "".join(i2.splitlines())
	r = len(map)
	c = len(map[0])

	i = 0
	j = 0

	for a in range(r):
		for b in range(c):
			if map[a][b] == "@":
				i = a
				j = b
				break

	def move(x, y, dir):
		nonlocal map

		c = map[x][y]
		if c == "#": return False
		if c == ".": return True

		xx = x + dir[0]
		yy = y + dir[1]
		is_vacant = move(xx, yy, dir)
		if is_vacant:
			map[x][y] = "."
			map[xx][yy] = c
			return True
		else:
			return False

	for step in path:
		mappings = {
			"<": (0, -1),
			"v": (1, 0),
			"^": (-1, 0),
			">": (0, 1),
		}

		dir = mappings[step]

		can_move = move(i, j, dir)
		if can_move:
			i += dir[0]
			j += dir[1]

	ans = 0

	for i in range(r):
		for j in range(c):
			if map[i][j] == "O":
				ans += i * 100 + j

	return ans
