from functools import cache
from itertools import permutations

nums = {
	" ": (3, 0),
	"A": (3, 2),
	"0": (3, 1),
	"1": (2, 0),
	"2": (2, 1),
	"3": (2, 2),
	"4": (1, 0),
	"5": (1, 1),
	"6": (1, 2),
	"7": (0, 0),
	"8": (0, 1),
	"9": (0, 2),
}

directions = {
	" ": (0, 0),
	"A": (0, 2),
	"<": (1, 0),
	"v": (1, 1),
	"^": (0, 1),
	">": (1, 2),
}

def find_seqs(a, b):
	is_nums = a in nums and b in nums
	grid = nums if is_nums else directions
	dx = grid[b][0] - grid[a][0]
	dy = grid[b][1] - grid[a][1]

	def is_valid(moves):
		(i, j) = grid[a]

		for c in moves:
			if c == "<":
				j -= 1
			elif c == "v":
				i += 1
			elif c == "^":
				i -= 1
			elif c == ">":
				j += 1

			if (i, j) == grid[" "]: return False

		return True

	moves = []

	for _ in range(abs(dx)):
		if dx > 0:
			moves.append("v")
		else:
			moves.append("^")

	for _ in range(abs(dy)):
		if dy > 0:
			moves.append(">")
		else:
			moves.append("<")

	s = set()
	for p in permutations(moves):
		s.add("".join(p) + "A")

	return list(moves for moves in s if is_valid(moves))

@cache
def expand_bigram(bigram, layers):
	a = bigram[0]
	b = bigram[1]

	seqs = find_seqs(a, b)

	if layers == 0:
		return len(min(seqs, key=len))

	expanded_seqs = [expand_path(x, layers - 1) for x in seqs]

	return min(expanded_seqs)

def expand_path(path, layers):
	ans = 0

	for i in range(len(path)):
		a = "A" if i == 0 else path[i - 1]
		b = path[i]
		ans += expand_bigram(a + b, layers)

	return ans

def solve(input):
	lines = input.splitlines()

	ans = 0
	for line in lines:
		num = int(line[:-1])
		length = expand_path(line, 2)
		ans += num * length

	return ans
