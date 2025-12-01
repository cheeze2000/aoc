def solve(input):
	lines = input.splitlines()

	num = 50
	zeros = 0

	for line in lines:
		count = int(line[1:])
		if line[0] == "L": count = -count

		zeros += intersection_count(num, count)
		num += count
		num %= 100

	return zeros

def intersection_count(num, count):
	full_circles = abs(count) // 100
	if num == 0: return full_circles

	if count >= 0:
		count -= full_circles * 100
		num += count

		if num >= 100:
			return full_circles + 1
		else:
			return full_circles
	else:
		count += full_circles * 100
		num += count

		if num <= 0:
			return full_circles + 1
		else:
			return full_circles
