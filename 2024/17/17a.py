import re

def solve(input):
	[regs, insts] = input.split("\n\n")
	[a, b, c] = [int(i) for i in re.findall(r"\d+", regs)]

	code = [int(i) for i in insts.split()[1].split(",")]

	i = 0
	output = []

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
			output.append(str(combo(operand) % 8))
		elif inst == 6:
			b = a // (2 ** combo(operand))
		elif inst == 7:
			c = a // (2 ** combo(operand))

		i += 2

	return ",".join(output)
