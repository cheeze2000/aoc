import sys

xs = set()
n = 0

def f(x, y):
	y = y + 1
	if y == n + 2:
		xs.add((x - 1, y))
		xs.add((x, y))
		xs.add((x + 1, y))

	if (x - 1, y) in xs and (x, y) in xs and (x + 1, y) in xs:
		xs.add((x, y - 1))
		if (x, y - 1) == (500, 0): return True
		return False

	if (x, y) not in xs: return f(x, y)
	if (x - 1, y) not in xs: return f(x - 1, y)
	if (x + 1, y) not in xs: return f(x + 1, y)

if __name__ == "__main__":
	for line in sys.stdin:
		ys = line.split(" -> ")
		for i in range(len(ys) - 1):
			a = [int(d) for d in ys[i].split(",")]
			b = [int(d) for d in ys[i + 1].split(",")]
			n = max(n, a[1], b[1])

			if a[0] == b[0]:
				[c, d] = sorted([a[1], b[1]])
				for k in range(c, d + 1): xs.add((a[0], k))
			else:
				[c, d] = sorted([a[0], b[0]])
				for k in range(c, d + 1): xs.add((k, a[1]))

	i = 1
	while True:
		if f(500, 0): break
		else: i += 1

	print(i)
