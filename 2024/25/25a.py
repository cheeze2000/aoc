def solve(input):
	items = input.split("\n\n")

	locks = []
	keys = []

	for item in items:
		lines = item.splitlines()
		lst = [0, 0, 0, 0, 0]

		for line in lines[1:-1]:
			for i in range(5):
				if line[i] == "#": lst[i] += 1

		if lines[0].startswith("#"):
			locks.append(lst)
		else:
			keys.append(lst)

	ans = 0

	for lock in locks:
		for key in keys:
			if all(lock[i] + key[i] <= 5 for i in range(5)):
				ans += 1

	return ans
