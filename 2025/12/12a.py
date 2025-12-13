from functools import cache

def solve(input):
	sections = input.split("\n\n")
	region_section = sections.pop()

	shapes = []
	regions = []

	for region_line in region_section.splitlines():
		[a, b] = region_line.split(": ")
		[c, r] = a.split("x")
		counts = b.split(" ")

		region = (int(r), int(c), [int(x) for x in counts])
		regions.append(region)

	for shape_section in sections:
		shape_lines = shape_section.splitlines()[1:]
		shape = []

		for line in shape_lines:
			shape.append([1 if x == "#" else 0 for x in line])

		shapes.append(shape)

	ans = 0

	for region in regions:
		if is_feasible(region) and can_fit_shapes(region, shapes):
			ans += 1

	return ans

def is_feasible(region):
	(r, c, counts) = region
	total_counts = sum(counts)

	rows = r // 3
	cols = c // 3

	return total_counts <= rows * cols

def can_fit_shapes(region, shapes):
	(r, c, counts) = region

	shape_areas = [
		sum(shape[i][j] for i in range(3) for j in range(3))
		for shape in shapes
	]

	transformations = []

	for shape in shapes:
		shape_transformations = [transform_shape(shape, t) for t in range(8)]
		transformations.append(shape_transformations)

	grid = [[0] * c for _ in range(r)]

	@cache
	def dfs(shape_index, position = 0):
		if shape_index == len(shapes):
			return True

		shape_count = counts[shape_index]

		if shape_count == 0:
			return dfs(shape_index + 1)

		total_shape_area = shape_areas[shape_index] * shape_count

		for pos in range(position, r * c):
			i = pos // c
			j = pos % c

			if (r * c) - pos < total_shape_area:
				return False

			for transformation in range(8):
				transformed_shape = transformations[shape_index][transformation]
				transformed_shape = can_place_shape_at(grid, transformed_shape, i, j)

				if transformed_shape is not None:
					place_shape_at(grid, transformed_shape, i, j)
					counts[shape_index] -= 1

					if dfs(shape_index, pos + 1):
						return True

					unplace_shape_at(grid, transformed_shape, i, j)
					counts[shape_index] += 1

		return False

	return dfs(0)

def can_place_shape_at(grid, shape, x, y):
	def get(i, j):
		if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
			return grid[i][j]

	for i in range(3):
		for j in range(3):
			if shape[i][j] == 0:
				continue

			cell = get(x + i, y + j)
			if cell == 1 or cell is None:
				return None

	return shape

def place_shape_at(grid, shape, x, y):
	for i in range(3):
		for j in range(3):
			if shape[i][j] == 0:
				continue

			grid[x + i][y + j] = 1

def unplace_shape_at(grid, shape, x, y):
	for i in range(3):
		for j in range(3):
			if shape[i][j] == 0:
				continue

			grid[x + i][y + j] = 0

def transform_shape(shape, num):
	new_shape = [[0] * 3 for _ in range(3)]

	for i in range(3):
		for j in range(3):
			if num == 0:
				new_shape[i][j] = shape[i][j]
			elif num == 1:
				new_shape[i][j] = shape[i][2 - j]
			elif num == 2:
				new_shape[i][j] = shape[2 - i][j]
			elif num == 3:
				new_shape[i][j] = shape[2 - i][2 - j]
			elif num == 4:
				new_shape[i][j] = shape[j][i]
			elif num == 5:
				new_shape[i][j] = shape[j][2 - i]
			elif num == 6:
				new_shape[i][j] = shape[2 - j][i]
			elif num == 7:
				new_shape[i][j] = shape[2 - j][2 - i]

	return new_shape
