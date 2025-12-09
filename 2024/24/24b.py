from functools import cache
import re

def solve(input):
	[data, equations] = input.split("\n\n")

	def solve_with_swaps(swaps):
		if len(swaps) == 4:
			flat = ",".join(sorted(list(s for swap in swaps for s in swap)))
			return flat

		gates = {}
		values = {}

		for eq in equations.splitlines():
			(g1, op, g2, target) = re.findall(r"(\w+) (\w+) (\w+) -> (\w+)", eq)[0]

			for (s1, s2) in swaps:
				if target == s1: target = s2
				elif target == s2: target = s1

			gates[target] = (g1, op, g2)

		for line in data.splitlines():
			[gate, value] = line.split(": ")
			values[gate] = int(value)

		def calculate(gate):
			if gate[0] == "x" or gate[0] == "y":
				return gate
			elif gate in values:
				return values[gate]

			(g1, op, g2) = gates[gate]
			val1 = calculate(g1)
			val2 = calculate(g2)
			result = (val1, op, val2)
			values[gate] = result
			return result

		def is_equal(ast1, ast2):
			if isinstance(ast1, str) and isinstance(ast2, str):
				return ast1 == ast2
			elif ast1[1] != ast2[1]:
				return False

			return (is_equal(ast1[0], ast2[0]) and is_equal(ast1[2], ast2[2])) or (is_equal(ast1[0], ast2[2]) and is_equal(ast1[2], ast2[0]))

		def investigate(zkey):
			index = int(zkey[1:])
			ast = calculate(zkey)
			for gate in gates:
				if is_equal(calculate(gate), expected_z(index)):
					swaps.append((zkey, gate))
					return

			for gate in gates:
				if is_equal(ast[0], expected_carry(index - 1)):
					target = gates[zkey][2]
				elif is_equal(ast[2], expected_carry(index - 1)):
					target = gates[zkey][0]
				else:
					continue

				for gate1 in gates:
					if is_equal(calculate(gate1), expected_a_xor_b(index)):
						swaps.append((target, gate1))
						return

		zkeys = [key for key in gates.keys() if key[0] == "z"]
		zkeys.sort()

		for zkey in zkeys:
			index = int(zkey[1:])

			is_correct = is_equal(calculate(zkey), expected_z(index))

			if not is_correct:
				investigate(zkey)
				return solve_with_swaps(swaps)

	return solve_with_swaps([])

# S = (A XOR B) XOR C_in
@cache
def expected_z(index):
	if index == 0:
		return ("x00", "XOR", "y00")

	a_xor_b = (f"x{index:02d}", "XOR", f"y{index:02d}")

	return (a_xor_b, "XOR", expected_carry(index - 1))

# A XOR B
@cache
def expected_a_xor_b(index):
	return (f"x{index:02d}", "XOR", f"y{index:02d}")

# C_out = (A AND B) OR (C_in AND (A XOR B))
@cache
def expected_carry(index):
	if index == 0:
		return ("x00", "AND", "y00")

	a_and_b = (f"x{index:02d}", "AND", f"y{index:02d}")
	a_xor_b = (f"x{index:02d}", "XOR", f"y{index:02d}")
	prev_carry = expected_carry(index - 1)

	return (a_and_b, "OR", (prev_carry, "AND", a_xor_b))
