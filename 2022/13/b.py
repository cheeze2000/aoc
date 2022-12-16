import json
import sys

def f(xs, ys):
	def i(x): return isinstance(x, int)

	if i(xs) and i(ys):
		if xs < ys: return 1
		elif xs == ys: return -1
		else: return 0
	elif not i(xs) and i(ys):
		return f(xs, [ys])
	elif i(xs) and not i(ys):
		return f([xs], ys)
	else:
		n = 0
		while True:
			if len(xs) == n and len(ys) == n: return -1
			if len(xs) == n: return 1
			if len(ys) == n: return 0

			m = f(xs[n], ys[n])
			if m == -1: n += 1
			else: return m

if __name__ == "__main__":
	a = 1
	b = -2
	c = 0
	while True:
		xs = json.loads(input())
		ys = json.loads(input())
		two = [[2]]
		six = [[6]]

		a += f(xs, two)
		a += f(ys, two)
		b += f(six, xs)
		b += f(six, ys)
		c += 2
		if sys.stdin.readline() == "": break

	print(a * (c - b))
