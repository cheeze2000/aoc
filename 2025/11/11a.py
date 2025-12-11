from functools import cache

def solve(input):
	lines = input.splitlines()

	graph = {}

	for line in lines:
		[a, b] = line.split(": ")
		graph[a] = b.split(" ")

	@cache
	def dfs(node):
		if node == "out":
			return 1

		paths = 0

		for neighbour in graph[node]:
			paths += dfs(neighbour)

		return paths

	return dfs("you")
