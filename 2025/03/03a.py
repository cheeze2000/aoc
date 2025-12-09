def solve(input):
	lines = input.splitlines()

	ans = 0

	for line in lines:
		nums = [int(x) for x in line]
		ans += joltage(nums)

	return ans

def joltage(nums):
	i = 0
	j = 0

	highest = 0

	while j < len(nums):
		if i == j:
			j += 1
			continue

		highest = max(highest, nums[i] * 10 + nums[j])

		if nums[i] < nums[j]:
			i = j
			j += 1
		else:
			j += 1

	return highest
