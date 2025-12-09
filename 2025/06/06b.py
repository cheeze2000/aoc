import math

def solve(input):
	lines = input.splitlines()
	operators = lines.pop()
	nums = lines

	separator_indices = [i - 1 for i, op in enumerate(operators) if op != " " and i > 0]

	for i in range(len(nums)):
		row = list(nums[i])
		for sep in separator_indices:
			row[sep] = "|"

		nums[i] = "".join(row).split("|")

	ans = 0

	operators = operators.split()
	for i in range(len(operators)):
		column = [row[i] for row in nums]
		n = max(len(entry) for entry in column)

		transposed = []
		for j in range(n - 1, -1, -1):
			num = [entry[j] for entry in column if j < len(entry) and entry[j] != " "]
			transposed.append(int("".join(num)))

		if operators[i] == "+":
			ans += sum(transposed)
		else:
			ans += math.prod(transposed)

	return ans
