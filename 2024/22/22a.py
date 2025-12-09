def solve(input):
	nums = [int(i) for i in input.splitlines()]

	ans = 0
	for num in nums:
		ans += next(num, 2000)

	return ans

def next(num, iterations=1):
	M = 16777216

	def step(num):
		num = num ^ (num * 64)
		num = num % M
		num = num ^ round(num // 32)
		num = num % M
		num = num ^ (num * 2048)
		num = num % M

		return num

	for _ in range(iterations):
		num = step(num)

	return num
