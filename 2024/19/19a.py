from functools import cache

def solve(input):
	[towels, patterns] = input.split("\n\n")

	towels = towels.split(", ")
	patterns = patterns.splitlines()

	ans = 0
	for pattern in patterns:
		if is_possible(towels, pattern): ans += 1

	return ans

def is_possible(towels, pattern):
	@cache
	def rec(index):
		if index == len(pattern): return True

		for towel in towels:
			if pattern.startswith(towel, index):
				if rec(index + len(towel)):
					return True

		return False

	return rec(0)
