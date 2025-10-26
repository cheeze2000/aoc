import re

def solve(input):
	claws = input.split("\n\n")
	ans = 0

	for claw in claws:
		lines = claw.splitlines()
		[ax, ay] = [int(i) for i in re.findall(r"\d+", lines[0])]
		[bx, by] = [int(i) for i in re.findall(r"\d+", lines[1])]
		[cx, cy] = [int(i) for i in re.findall(r"\d+", lines[2])]

		min_sum = 1e9

		for an in range(101):
			tx = cx - ax * an
			ty = cy - ay * an

			if (tx % bx != 0) or (ty % by != 0): continue
			if (tx // bx) != (ty // by): continue

			bn = tx // bx

			min_sum = min(min_sum, an * 3 + bn)

		if min_sum != 1e9: ans += min_sum

	return ans
