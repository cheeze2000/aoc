from collections import defaultdict

def solve(input):
	[pairs, lines] = input.split("\n\n")

	rules = []
	for pair in pairs.splitlines():
		[a, b] = pair.split("|")
		rules.append((int(a), int(b)))

	ans = 0

	for line in lines.splitlines():
		nums = [int(l) for l in line.split(",")]
		sorted_nums = sort_with_rules(nums, rules)

		if nums == sorted_nums: ans += nums[len(nums) // 2]

	return ans

def sort_with_rules(nums, rules):
	nums_set = set(nums)
	new_rules = [rule for rule in rules if rule[0] in nums_set and rule[1] in nums_set]

	ordering = topo_sort(new_rules)

	return ordering[::-1]


def topo_sort(rules):
	graph = defaultdict(list)
	for a, b in rules:
		graph[a].append(b)

	ordering = []
	visited = set()

	def dfs(node):
		if node in visited: return
		visited.add(node)

		for n in graph[node]: dfs(n)

		ordering.append(node)

	for node in list(graph):
		dfs(node)

	return ordering
