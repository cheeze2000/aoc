from functools import cache

def solve(input):
	nums = [int(i) for i in input.split()]

	return sum(count(num, 25) for num in nums)

@cache
def count(num, blinks):
	if blinks == 0: return 1

	s = str(num)
	if num == 0:
		return count(1, blinks - 1)
	elif len(s) % 2 == 0:
		a = int(s[:len(s)//2])
		b = int(s[len(s)//2:])
		return count(a, blinks - 1) + count(b, blinks - 1)
	else:
		return count(num * 2024, blinks - 1)
