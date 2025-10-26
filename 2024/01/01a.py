def solve(input):
	lines = input.splitlines()

	xs = []
	ys = []

	for line in lines:
		a, b = (int(i) for i in line.split())
		xs.append(a)
		ys.append(b)

	xs.sort()
	ys.sort()

	ans = 0
	for i in range(len(xs)):
		ans += abs(xs[i] - ys[i])

	return ans
