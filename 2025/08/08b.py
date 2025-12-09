import math

def solve(input):
	lines = input.splitlines()

	boxes = []

	for line in lines:
		[x, y, z] = line.split(",")
		boxes.append((int(x), int(y), int(z)))

	n = len(boxes)
	distances = []

	for i in range(n):
		for j in range(i + 1, n):
			(x1, y1, z1) = boxes[i]
			(x2, y2, z2) = boxes[j]
			sum = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
			distances.append((sum ** 0.5, i, j))

	disj = {i: i for i in range(n)}
	size = n

	def parent(i):
		if disj[i] == i:
			return i

		disj[i] = parent(disj[i])
		return disj[i]

	def unify(i, j):
		nonlocal size

		pi = parent(i)
		pj = parent(j)

		if pi != pj:
			size -= 1

		disj[pi] = pj

	for (_, i, j) in sorted(distances):
		unify(i, j)

		if size == 1:
			x1 = boxes[i][0]
			x2 = boxes[j][0]
			return x1 * x2
