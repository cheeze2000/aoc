from collections import defaultdict, deque

def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	sx = 0
	sy = 0
	ex = 0
	ey = 0
	for i in range(r):
		for j in range(c):
			if map[i][j] == "S":
				sx = i
				sy = j
			if map[i][j] == "E":
				ex = i
				ey = j

	q = deque()
	q.append((0, sx, sy))
	dist = defaultdict(lambda: float("inf"))

	while len(q) > 0:
		(d, i, j) = q.popleft()
		if i < 0 or i >= r or j < 0 or j >= c: continue
		if map[i][j] == "#": continue

		if (i, j) in dist: continue
		dist[(i, j)] = d

		q.append((d + 1, i - 1, j))
		q.append((d + 1, i + 1, j))
		q.append((d + 1, i, j - 1))
		q.append((d + 1, i, j + 1))

	q = deque()
	q.append((0, sx, sy, (-1, -1), None))

	finishes = defaultdict(lambda: 0)
	visited = set()

	while len(q) > 0:
		(d, i, j, src, cheat) = q.popleft()
		if i < 0 or i >= r or j < 0 or j >= c: continue
		if d > dist[(ex, ey)]: continue
		if (i, j, src, cheat) in visited: continue
		visited.add((i, j, src, cheat))

		if map[i][j] == "#":
			if cheat is None:
				q.append((d + 1, i - 1, j, src, (i, j)))
				q.append((d + 1, i + 1, j, src, (i, j)))
				q.append((d + 1, i, j - 1, src, (i, j)))
				q.append((d + 1, i, j + 1, src, (i, j)))
			else:
				continue
		else:
			if cheat is None:
				q.append((d + 1, i - 1, j, (i, j), None))
				q.append((d + 1, i + 1, j, (i, j), None))
				q.append((d + 1, i, j - 1, (i, j), None))
				q.append((d + 1, i, j + 1, (i, j), None))
			else:
				finishes[d + dist[(ex, ey)] - dist[(i, j)]] += 1

	ans = 0

	for (k, v) in finishes.items():
		if k <= dist[(ex, ey)] - 100: ans += v

	return ans
