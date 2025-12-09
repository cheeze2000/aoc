from collections import defaultdict
from itertools import combinations

def solve(input):
	graph = defaultdict(set)

	for line in input.splitlines():
		a, b = line.split("-")
		graph[a].add(b)
		graph[b].add(a)

	def is_complete(nodes):
		for i in range(len(nodes)):
			a = nodes[i]
			for j in range(i + 1, len(nodes)):
				b = nodes[j]
				if a not in graph[b]:
					return False

		return True

	complete = []

	for node, neighbours in graph.items():
		for i in range(len(neighbours) - 1, len(complete) - 1, -1):
			for combo in combinations(neighbours, i):
				if not is_complete(combo): continue

				kn = list(combo) + [node]

				if len(kn) > len(complete):
					complete = kn

					i = 0
					break

	return ",".join(sorted(complete))
