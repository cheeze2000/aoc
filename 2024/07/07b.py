from functools import cache
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
	@cache
	def dfs(i, acc):
		num = nums[i - 1]

		if i == 1: return acc == num

		p1 = str(acc).endswith(str(num))
		p2 = acc % num == 0
		p3 = acc >= num

		result = False

		if p1 and len(str(acc)) > len(str(num)):
			result |= dfs(i - 1, int(str(acc)[:-len(str(num))]) )
		if p2: result |= dfs(i - 1, acc // num)
		if p3: result |= dfs(i - 1, acc - num)

		return result

	if dfs(len(nums), target): return target
	else: return 0
