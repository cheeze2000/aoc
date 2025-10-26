from functools import cache

def solve(input):
	[regs, insts] = input.split("\n\n")
	code = [int(i) for i in insts.split()[1].split(",")]

	a = 0

	@cache
	def dfs(index, a):
		if index < 0: return a
		target = code[index]

		for i in range(a * 8, a * 8 + 8):
			if get_output(code, i, 0, 0) == target:
				result = dfs(index - 1, i)

				if result > -1: return result

		return -1

	return dfs(len(code) - 1, 0)

def get_output(code, a, b, c):
	i = 0

	while i < len(code):
		inst = code[i]
		operand = code[i + 1]

		def combo(operand):
			if 0 <= operand <= 3: return operand
			elif operand == 4: return a
			elif operand == 5: return b
			else: return c

		if inst == 0:
			a = a // (2 ** combo(operand))
		elif inst == 1:
			b = b ^ operand
		elif inst == 2:
			b = combo(operand) % 8
		elif inst == 3:
			if a != 0:
				i = operand - 2
		elif inst == 4:
			b = b ^ c
		elif inst == 5:
			return combo(operand) % 8
		elif inst == 6:
			b = a // (2 ** combo(operand))
		elif inst == 7:
			c = a // (2 ** combo(operand))

		i += 2
