def solve(input):
	ranges = []

	for s in input.split(","):
		[start, end] = s.split("-")
		ranges.append((int(start), int(end)))

	ans = 0

	for (start, end) in ranges:
		ans += invalid_count(start, end)

	return ans

def invalid_count(start, end):
	start_len = len(str(start))
	end_len = len(str(end))

	if start_len % 2 == 0:
		i = int(str(start)[:start_len // 2])
	else:
		i = 10 ** (start_len // 2) - 1

	if end_len % 2 == 0:
		j = int(str(end)[:end_len // 2])
	else:
		j = 10 ** (end_len // 2) - 1

	ans = 0

	for k in range(i, j + 1):
		id = int(str(k) * 2)

		if start <= id <= end:
			ans += id

	return ans
