def solve(input):
	[i1, i2] = input.split("\n\n")
	map = [[]]
	for c in i1:
		if c == "\n":
			map.append([])
		elif c == "#":
			map[-1].append("#")
			map[-1].append("#")
		elif c == "O":
			map[-1].append("[")
			map[-1].append("]")
		elif c == ".":
			map[-1].append(".")
			map[-1].append(".")
		else:
			map[-1].append("@")
			map[-1].append(".")

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

	def move(x, y, dir, mutate=True):
		nonlocal map

		c = map[x][y]
		if c == "#": return False
		if c == ".": return True

		(dx, dy) = dir
		xx = x + dx
		yy = y + dy

		is_vertical = dir == (1, 0) or dir == (-1, 0)

		if c == "[" and is_vertical:
			is_vacant = move(xx, yy, dir, False) and move(xx, yy + 1, dir, False)
			if is_vacant:
				move(xx, yy, dir, mutate)
				move(xx, yy + 1, dir, mutate)
		elif c == "]" and is_vertical:
			is_vacant = move(xx, yy, dir, False) and move(xx, yy - 1, dir, False)
			if is_vacant:
				move(xx, yy, dir, mutate)
				move(xx, yy - 1, dir, mutate)
		else:
			is_vacant = move(xx, yy, dir, mutate)

		if mutate and is_vacant:
			if c == "[" and is_vertical:
				map[x][y] = "."
				map[x][y + 1] = "."
				map[xx][yy] = "["
				map[xx][yy + 1] = "]"
			elif c == "]" and is_vertical:
				map[x][y] = "."
				map[x][y - 1] = "."
				map[xx][yy] = "]"
				map[xx][yy - 1] = "["
			else:
				map[x][y] = "."
				map[xx][yy] = c

		return is_vacant

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
			if map[i][j] == "[":
				ans += i * 100 + j

	return ans
