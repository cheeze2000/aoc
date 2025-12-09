def solve(input):
	lines = input.splitlines()

	coords = []

	for line in lines:
		[x, y] = line.split(",")
		coords.append((int(x), int(y)))

	n = len(coords)
	ans = 0

	def is_valid_rectangle(x1, y1, x2, y2):
		x1, x2 = min(x1, x2), max(x1, x2)
		y1, y2 = min(y1, y2), max(y1, y2)

		for i in range(n):
			j = (i + 1) % n

			xi, yi = coords[i]
			xj, yj = coords[j]

			xi, xj = min(xi, xj), max(xi, xj)
			yi, yj = min(yi, yj), max(yi, yj)

			if xi == xj:
				if x1 < xi < x2 and yi < y2 and y1 < yj:
					return False
			else:
				if y1 < yi < y2 and xi < x2 and x1 < xj:
					return False

		return True

	rectangles = []

	for i in range(n):
		for j in range(i + 1, n):
			(x1, y1) = coords[i]
			(x2, y2) = coords[j]

			area = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
			rectangles.append((area, x1, y1, x2, y2))

	rectangles.sort()

	while len(rectangles) > 0:
		(area, x1, y1, x2, y2) = rectangles.pop()

		if is_valid_rectangle(x1, y1, x2, y2):
			return area

	return ans
