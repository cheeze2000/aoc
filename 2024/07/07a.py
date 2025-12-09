import re

def solve(input):
	lines = input.splitlines()

	ans = 0

	for line in lines:
		target = int(re.match(r"(\d+):", line)[1])
		nums = [int(i) for i in re.search(r".+: (.+)", line)[1].split(" ")]

		ans += is_possible(nums, target)

	return ans

def is_possible(nums, target):
	n = len(nums)

	for i in range(2 ** (n - 1)):
		p2 = i

		acc = nums[0]

		for j in range(1, n):
			if p2 & 1: acc += nums[j]
			else: acc *= nums[j]

			p2 //= 2
			if acc > target: break

		if acc == target: return target

	return 0
