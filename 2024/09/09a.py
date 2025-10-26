def solve(input):
	row = []

	for i in range(len(input)):
		num = int(input[i])

		if i % 2 == 0:
			row.append((i // 2, num))
		else:
			row.append((-1, num))

	ans = 0
	n = 0

	i = 0
	j = len(row) - 1

	while i < j:
		(id1, size1) = row[i]
		(id2, size2) = row[j]

		if size1 == 0 or id1 > -1:
			i += 1
			ans += sum(range(n, n + size1)) * id1
			n += size1

			continue

		if size2 == 0 or id2 == -1:
			j -= 1
			continue

		to_move = min(size1, size2)
		row[i] = (id1, size1 - to_move)
		row[j] = (id2, size2 - to_move)

		ans += sum(range(n, n + to_move)) * id2
		n += to_move

	return ans
