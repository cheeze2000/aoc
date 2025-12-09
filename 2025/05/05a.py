def solve(input):
	[section1, section2] = input.split("\n\n")

	ranges = []
	ingredients = []

	for line in section1.splitlines():
		[a, b] = line.split("-")
		ranges.append((int(a), int(b)))

	for line in section2.splitlines():
		ingredients.append(int(line))

	ans = 0

	for ingredient in ingredients:
		fresh = False

		for (start, end) in ranges:
			fresh |= start <= ingredient <= end

		if fresh:
			ans += 1

	return ans
