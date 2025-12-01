def solve(input):
	lines = input.splitlines()

	num = 50
	zeros = 0

	for line in lines:
		count = int(line[1:])
		if line[0] == "L": count = -count

		num += count
		num %= 100

		if num == 0: zeros += 1

	return zeros
