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
	q.append((0, sx, sy))

	finishes = defaultdict(lambda: 0)
	visited = set()

	while len(q) > 0:
		(d, i, j) = q.popleft()
		if i < 0 or i >= r or j < 0 or j >= c: continue
		if map[i][j] == "#": continue
		if (i, j) in visited: continue
		visited.add((i, j))

		if i == ex and j == ey: continue

		for di in range(-20, 21):
			for dj in range(-20, 21):
				cheat = abs(di) + abs(dj)
				if cheat > 20: continue
				ii = i + di
				jj = j + dj
				if ii < 0 or ii >= r or jj < 0 or jj >= c: continue
				if map[ii][jj] == "#": continue
				finishes[d + cheat + dist[(ex, ey)] - dist[(ii, jj)]] += 1

		q.append((d + 1, i - 1, j))
		q.append((d + 1, i + 1, j))
		q.append((d + 1, i, j - 1))
		q.append((d + 1, i, j + 1))

	ans = 0

	for (k, v) in finishes.items():
		if k <= dist[(ex, ey)] - 100: ans += v

	return ans
