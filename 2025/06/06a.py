import math

def solve(input):
	lines = input.splitlines()
	nums = [line.split() for line in lines]
	operators = nums.pop()

	ans = 0

	for i in range(len(operators)):
		column = [int(row[i]) for row in nums]
		if operators[i] == "+":
			ans += sum(column)
		else:
			ans += math.prod(column)

	return ans
