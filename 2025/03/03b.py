from functools import cache

def solve(input):
	lines = input.splitlines()

	ans = 0

	for line in lines:
		nums = [int(x) for x in line]
		ans += joltage(nums)

	return ans

def joltage(nums):
	@cache
	def highest(i, count):
		if count == 0:
			return 0

		ans = nums[i] * 10 ** (count - 1) + highest(i + 1, count - 1)

		if len(nums) - i > count:
			ans = max(ans, highest(i + 1, count))

		return ans

	return highest(0, 12)
