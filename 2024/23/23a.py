from collections import defaultdict

def solve(input):
	graph = defaultdict(set)

	for line in input.splitlines():
		a, b = line.split("-")
		graph[a].add(b)
		graph[b].add(a)

	ts = list(key for key in graph.keys() if key[0] == "t")

	triples = set()

	for comp in ts:
		neighbours = list(graph[comp])

		for i in range(len(neighbours)):
			for j in range(i + 1, len(neighbours)):
				a = neighbours[i]
				b = neighbours[j]

				if b not in graph[a]: continue
				[x, y, z] = sorted([a, b, comp])
				triples.add((x, y, z))

	return len(triples)
