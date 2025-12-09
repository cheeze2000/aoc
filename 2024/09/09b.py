def solve(input):
	files = []
	spaces = []

	n = 0
	for i in range(len(input)):
		num = int(input[i])

		if i % 2 == 0:
			files.append((n, num, i // 2))
		else:
			spaces.append((n, num))

		n += num

	n = len(files)

	for i in range(n - 1, -1, -1):
		(index, size, id) = files[i]

		for j in range(i):
			(index1, size1) = spaces[j]
			if size1 < size: continue

			spaces[j] = (index1 + size, size1 - size)
			files[i] = (index1, size, id)
			break

	ans = 0
	for (index, size, id) in files:
		ans += sum(range(index, index + size)) * id

	return ans
