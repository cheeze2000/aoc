import re

def solve(input):
	robots = []
	width = 101
	height = 103

	for line in input.splitlines():
		coords = re.findall(r"-?\d+", line)
		robots.append(tuple(int(x) for x in coords))

	new_robots = []
	for (i, j, vx, vy) in robots:
		ii = i + vx * 100
		jj = j + vy * 100
		new_robots.append((ii % width, jj % height, vx, vy))

	q1 = 0
	q2 = 0
	q3 = 0
	q4 = 0

	for (i, j, vx, vy) in new_robots:
		if j < (height // 2):
			if i < (width // 2):
				q2 += 1
			elif i > (width // 2):
				q1 += 1
		elif j > (height // 2):
			if i < (width // 2):
				q3 += 1
			elif i > (width // 2):
				q4 += 1

	return q1 * q2 * q3 * q4
