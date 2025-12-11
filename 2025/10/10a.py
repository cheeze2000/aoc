import re

def solve(input):
	lines = input.splitlines()

	ans = 0

	for line in lines:
		lights = re.findall(r"\[(.+)\]", line)[0]
		lights = [c == "#" for c in lights]

		buttons = re.findall(r"\(([^)]+)\)", line)
		buttons = [list(map(int, b.split(","))) for b in buttons]

		ans += fewest_presses(lights, buttons)

	return ans

def fewest_presses(lights, buttons):
	L = len(lights)
	B = len(buttons)

	ans = float("inf")

	for i in range(1 << B):
		state = [False] * L
		bitset = bin(i)[2:].zfill(B)

		for j in range(B):
			if bitset[j] == "1":
				for index in buttons[j]:
					state[index] = not state[index]

		if state == lights:
			ans = min(ans, bitset.count("1"))

	return ans
