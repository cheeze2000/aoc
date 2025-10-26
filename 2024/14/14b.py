import re

def solve(input):
	robots = []
	width = 101
	height = 103

	for line in input.splitlines():
		coords = re.findall(r"-?\d+", line)
		robots.append(tuple(int(x) for x in coords))

	for i in range(int(1e9)):
		if "#########" in render(robots, width, height):
			return i

		robots = next(robots, width, height)


def next(robots, width, height):
	new_robots = []
	for (i, j, vx, vy) in robots:
		ii = i + vx
		jj = j + vy
		new_robots.append((ii % width, jj % height, vx, vy))

	return new_robots

def render(robots, width, height):
	grid = [["."] * width for _ in range(height)]
	for (i, j, vx, vy) in robots:
		grid[j][i] = "#"

	return "".join("".join(row) for row in grid)
