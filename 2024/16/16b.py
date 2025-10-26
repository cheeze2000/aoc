from collections import defaultdict, deque
import heapq

def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	i = 0
	j = 0
	k = 1
	gx = 0
	gy = 0

	for a in range(r):
		for b in range(c):
			if map[a][b] == "S":
				i = a
				j = b
			if map[a][b] == "E":
				gx = a
				gy = b

	dist = defaultdict(lambda: int(1e9))
	before = defaultdict(set)
	q = []
	heapq.heappush(q, (0, i, j, k))

	while len(q) > 0:
		(d, x, y, dir) = heapq.heappop(q)
		if map[x][y] == "#": continue
		if dist[(x, y, dir)] < d: continue
		dist[(x, y, dir)] = d

		dirleft = (dir + 3) % 4
		dirright = (dir + 1) % 4
		if dist[(x, y, dirleft)] >= d + 1000:
			if dist[(x, y, dirleft)] > d + 1000:
				heapq.heappush(q, (d + 1000, x, y, dirleft))
				dist[(x, y, dirleft)] = d + 1000
				before[(x, y, dirleft)] = { (x, y, dir) }
			else:
				before[(x, y, dirleft)].add((x, y, dir))
		if dist[(x, y, dirright)] >= d + 1000:
			if dist[(x, y, dirright)] > d + 1000:
				heapq.heappush(q, (d + 1000, x, y, dirright))
				dist[(x, y, dirright)] = d + 1000
				before[(x, y, dirright)] = { (x, y, dir) }
			else:
				before[(x, y, dirright)].add((x, y, dir))

		xx = x + dirs[dir][0]
		yy = y + dirs[dir][1]
		if dist[(xx, yy, dir)] >= d + 1:
			if dist[(xx, yy, dir)] > d + 1:
				heapq.heappush(q, (d + 1, xx, yy, dir))
				dist[(xx, yy, dir)] = d + 1
				before[(xx, yy, dir)] = { (x, y, dir) }
			else:
				before[(xx, yy, dir)].add((x, y, dir))

	mindist = min(dist[(gx, gy, d)] for d in range(4))

	q = deque()
	ans = set()

	for d in range(4):
		if dist[(gx, gy, d)] == mindist:
			q.append((gx, gy, d))

	while len(q) > 0:
		(x, y, dir) = q.popleft()
		ans.add((x, y))

		if x == i and y == j: continue

		for b in before[(x, y, dir)]: q.append(b)

	return len(ans)
