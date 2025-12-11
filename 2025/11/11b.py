from functools import cache

def solve(input):
	lines = input.splitlines()

	graph = {}

	for line in lines:
		[a, b] = line.split(": ")
		graph[a] = b.split(" ")

	def count_paths(start, end):
		@cache
		def dfs(node):
			if node == end:
				return 1

			paths = 0

			for neighbour in graph.get(node, []):
				paths += dfs(neighbour)

			return paths

		return dfs(start)

	fft_dac = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")
	dac_fft = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")

	return fft_dac + dac_fft
