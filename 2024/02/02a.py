def solve(input):
	lines = input.splitlines()

	ans = 0

	for line in lines:
		nums = [int(i) for i in line.split()]
		if is_safe(nums): ans += 1

	return ans

def is_safe(nums):
	d = nums[1] - nums[0]
	if d == 0 or abs(d) > 3: return False
	increasing = d > 0

	for i in range(1, len(nums) - 1):
		d = nums[i + 1] - nums[i]

		if increasing and d <= 0:
			return False

		if not increasing and d >= 0:
			return False

		if abs(d) > 3:
			return False

	return True
