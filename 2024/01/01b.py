from collections import Counter

def solve(input):
	lines = input.splitlines()

	xs = []
	ys = []

	for line in lines:
		a, b = (int(i) for i in line.split())
		xs.append(a)
		ys.append(b)

	counter = Counter(ys)

	ans = 0
	for x in xs:
		ans += counter[x] * x

	return ans
