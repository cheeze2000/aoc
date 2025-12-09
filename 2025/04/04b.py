from collections import defaultdict
from heapq import heappop, heappush

def solve(input):
	grid = input.splitlines()
	r = len(grid)
	c = len(grid[0])

	def get(i, j):
		if 0 <= i < r and 0 <= j < c:
			return grid[i][j]

	def neighbours(i, j):
		ans = []

		for di in [-1, 0, 1]:
			for dj in [-1, 0, 1]:
				if di == 0 and dj == 0:
					continue
				if get(i + di, j + dj) == "@":
					ans.append((i + di, j + dj))

		return ans

	neighbour_counts = {}
	heap = []

	for i in range(r):
		for j in range(c):
			if get(i, j) == "@":
				neighbour_count = len(neighbours(i, j))
				neighbour_counts[(i, j)] = neighbour_count
				heappush(heap, (neighbour_count, i, j))

	removed = 0

	while heap[0][0] < 4:
		(_, i, j) = heappop(heap)

		if (i, j) in neighbour_counts:
			del neighbour_counts[(i, j)]
			removed += 1
		else:
			continue

		for (ni, nj) in neighbours(i, j):
			if (ni, nj) in neighbour_counts:
				neighbour_counts[(ni, nj)] -= 1
				heappush(heap, (neighbour_counts[(ni, nj)], ni, nj))

	return removed
