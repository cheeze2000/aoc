def solve(input):
	[section1, section2] = input.split("\n\n")

	ranges = []

	for line in section1.splitlines():
		[a, b] = line.split("-")
		ranges.append((int(a), int(b)))

	ranges.sort()

	merged = []

	for (start, end) in ranges:
		if not merged or merged[-1][1] < start:
			merged.append([start, end])
		else:
			merged[-1][1] = max(merged[-1][1], end)

	ans = 0

	for (start, end) in merged:
		ans += end - start + 1

	return ans
