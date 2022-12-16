import sys

xs = set()
n = 0

def f(x, y):
	if y > n: return True

	y = y + 1
	if (x - 1, y) in xs and (x, y) in xs and (x + 1, y) in xs:
		xs.add((x, y - 1))
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

	i = 0
	while True:
		if f(500, 0): break
		else: i += 1

	print(i)
