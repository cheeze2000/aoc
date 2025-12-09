import re

def solve(input):
	results = re.findall(r"mul\((\d+),(\d+)\)", input)

	ans = 0
	for a, b in results: ans += int(a) * int(b)

	return ans
