def solve(input):
	map = [list(line) for line in input.splitlines()]
	r = len(map)
	c = len(map[0])

	ans = 0

	for i in range(r):
		for j in range(c):
			if map[i][j] != "A": continue

			ans += is_xmas(map, i, j)

	return ans

def is_xmas(map, x, y):
	def get(i, j):
		if 0 <= i < len(map) and 0 <= j < len(map[0]):
			return map[i][j]
		return ""

	ms1 = get(x - 1, y - 1) + get(x + 1, y + 1)
	ms2 = get(x - 1, y + 1) + get(x + 1, y - 1)

	if (ms1 == "MS" or ms1 == "SM") and (ms2 == "MS" or ms2 == "SM"):
		return 1

	return 0
