import re

def solve(input):
	claws = input.split("\n\n")
	ans = 0

	for claw in claws:
		lines = claw.splitlines()
		[ax, ay] = [int(i) for i in re.findall(r"\d+", lines[0])]
		[bx, by] = [int(i) for i in re.findall(r"\d+", lines[1])]
		[cx, cy] = [int(i) for i in re.findall(r"\d+", lines[2])]
		cx += 10000000000000
		cy += 10000000000000

		ar = ay / ax
		bn = round((cy - ar * cx) / (by - ar * bx))
		an = (cx - bn * bx) // ax

		if ax * an + bx * bn == cx and ay * an + by * bn == cy:
			ans += an * 3 + bn

	return ans
