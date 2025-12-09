def solve(input):
	lines = input.splitlines()

	coords = []

	for line in lines:
		[x, y] = line.split(",")
		coords.append((int(x), int(y)))

	n = len(coords)
	ans = 0

	for i in range(n):
		for j in range(i + 1, n):
			(x1, y1) = coords[i]
			(x2, y2) = coords[j]

			area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
			ans = max(ans, area)

	return ans
