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

	invalid_ids = set()

	for n in range(2, max(start_len, end_len) + 1):
		if start_len % n == 0:
			i = int(str(start)[:start_len // n])
		else:
			i = 10 ** (start_len // n) - 1

		if end_len % n == 0:
			j = int(str(end)[:end_len // n])
		else:
			j = 10 ** (end_len // n) - 1

		for k in range(i, j + 1):
			id = int(str(k) * n)

			if start <= id <= end:
				invalid_ids.add(id)

	return sum(invalid_ids)
