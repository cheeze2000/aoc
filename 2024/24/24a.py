import re

def solve(input):
	[data, equations] = input.split("\n\n")

	values = {}
	gates = {}

	for line in data.splitlines():
		[gate, value] = line.split(": ")
		values[gate] = int(value)

	for eq in equations.splitlines():
		(g1, op, g2, target) = re.findall(r"(\w+) (\w+) (\w+) -> (\w+)", eq)[0]

		op_lambda = {
			"AND": lambda a, b: a & b,
			"OR": lambda a, b: a | b,
			"XOR": lambda a, b: a ^ b,
		}

		gates[target] = (g1, op_lambda[op], g2)

	def calculate(gate):
		if gate in values:
			return values[gate]

		(g1, op, g2) = gates[gate]
		val1 = calculate(g1)
		val2 = calculate(g2)
		result = op(val1, val2)
		values[gate] = result
		return result

	for gate in gates.keys(): calculate(gate)

	zkeys = [key for key in values.keys() if key[0] == "z"]
	zkeys.sort(reverse=True)
	zvalues = [str(values[key]) for key in zkeys]

	return int("".join(zvalues), base=2)
