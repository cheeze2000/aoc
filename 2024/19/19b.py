from functools import cache

def solve(input):
	[towels, patterns] = input.split("\n\n")

	towels = towels.split(", ")
	patterns = patterns.splitlines()

	ans = 0
	for pattern in patterns:
		ans += is_possible(towels, pattern)

	return ans

def is_possible(towels, pattern):
	@cache
	def rec(index):
		if index == len(pattern): return 1

		ans = 0
		for towel in towels:
			if pattern.startswith(towel, index):
				ans += rec(index + len(towel))

		return ans

	return rec(0)
