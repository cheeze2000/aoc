import re

def iszero(x):
	return abs(x) < 1e-6

def solve(input):
	lines = input.splitlines()

	ans = 0

	for line in lines:
		buttons = re.findall(r"\(([^)]+)\)", line)
		buttons = [list(map(int, b.split(","))) for b in buttons]

		joltage = re.findall(r"\{(.+)\}", line)[0]
		joltage = [int(x) for x in joltage.split(",")]

		ans += fewest_presses(buttons, joltage)

	return ans

def fewest_presses(buttons, joltage):
	equations = []

	for i in range(len(joltage)):
		equation_terms = []

		for j in range(len(buttons)):
			if i in buttons[j]:
				equation_terms.append(j)

		equations.append((equation_terms, joltage[i]))

	equations = simplify_equations(buttons, equations)

	return solve_equations(equations, joltage)

def simplify_equations(buttons, equations):
	n = len(buttons)
	rows = []

	for eq in equations:
		(terms, expected_sum) = eq

		row = [0] * (n + 1)
		for term in terms:
			row[term] = 1

		row[-1] = expected_sum
		rows.append(row)

	ToReducedRowEchelonForm(rows)

	equations = []

	for row in rows:
		if all(iszero(x) for x in row):
			continue

		equations.append((row[:-1], row[-1]))

	return equations

# copied from https://rosettacode.org/wiki/Reduced_row_echelon_form
def ToReducedRowEchelonForm(M):
	lead = 0
	rowCount = len(M)
	columnCount = len(M[0])

	for r in range(rowCount):
		if lead >= columnCount:
			return
		i = r
		while iszero(M[i][lead]):
			i += 1
			if i == rowCount:
				i = r
				lead += 1
				if columnCount == lead:
					return
		M[i], M[r] = M[r], M[i]
		lv = M[r][lead]
		M[r] = [mrx / lv for mrx in M[r]]
		for i in range(rowCount):
			if i != r:
				lv = M[i][lead]
				M[i] = [iv - lv * rv for rv, iv in zip(M[r], M[i])]
		lead += 1

def solve_equations(equations, joltage):
	n = len(equations[0][0])
	max_presses = max(joltage)

	solutions = []

	def rec(index, assignments):
		if index == len(equations):
			solutions.append(assignments)
			return

		(terms, expected_sum) = equations[index]

		sum = 0
		presses = 0

		indices = [i for i in range(n) if not iszero(terms[i])]
		unknown_indices = [i for i in indices if assignments[i] is None]
		known_indices = [i for i in indices if assignments[i] is not None]

		for i in known_indices:
			sum += terms[i] * assignments[i]
			presses += assignments[i]

		for i in unknown_indices:
			r = range(0, max_presses - presses + 1)

			if len(unknown_indices) == 1:
				remaining = expected_sum - sum
				m = round(remaining / terms[i])

				if m < 0:
					r = range(0, 0)
				else:
					r = range(m, m + 1)

			for val in r:
				new_assignments = assignments[:]
				new_assignments[i] = val
				rec(index, new_assignments)

			return

		if iszero(sum - expected_sum):
			rec(index + 1, assignments)
		else:
			return

	rec(0, [None] * n)

	min_solution = min(solutions, key=sum)

	return sum(min_solution)
