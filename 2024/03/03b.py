import re

def solve(input):
	results = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)

	ans = 0
	enabled = True

	for result in results:
		if result.startswith("mul"):
			if enabled:
				a, b = re.findall(r"\d+", result)
				ans += int(a) * int(b)
		elif result.startswith("don"):
			enabled = False
		else:
			enabled = True

	return ans
