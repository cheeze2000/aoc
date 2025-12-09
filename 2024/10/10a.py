from collections import deque

def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	q = deque()
	visited = set()

	for i in range(r):
		for j in range(c):
			if map[i][j] == "0":
				q.append((i, j, i, j, 0))

	ans = 0

	while len(q) > 0:
		(si, sj, i, j, h) = q.popleft()
		if i < 0 or i >= r or j < 0 or j >= c: continue
		if map[i][j] != str(h): continue
		if (si, sj, i, j) in visited: continue
		visited.add((si, sj, i, j))

		if h == 9:
			ans += 1
		else:
			q.append((si, sj, i - 1, j, h + 1))
			q.append((si, sj, i, j + 1, h + 1))
			q.append((si, sj, i + 1, j, h + 1))
			q.append((si, sj, i, j - 1, h + 1))

	return ans
