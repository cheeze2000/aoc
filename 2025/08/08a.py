from collections import defaultdict
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

	def parent(i):
		if disj[i] == i:
			return i

		disj[i] = parent(disj[i])
		return disj[i]

	def unify(i, j):
		pi = parent(i)
		pj = parent(j)

		disj[pi] = pj

	for (_, i, j) in sorted(distances)[:1000]:
		unify(i, j)

	circuits = defaultdict(int)

	for i in range(n):
		circuits[parent(i)] += 1

	values = list(circuits.values())
	values.sort()

	return math.prod(values[-3:])
