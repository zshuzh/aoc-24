from itertools import product

with open('input.txt', 'r') as f:  
	matrix = f.read().splitlines()

def in_bounds(coord):
	i, j = coord

	if i < 0 or i >= len(matrix):
		return False
	if j < 0 or j >= len(matrix[0]):
		return False

	return True

def scan(coord, offset, str_i):
		i, j = coord
		di, dj = offset

		ii = i + di
		jj = j + dj

		if not in_bounds((ii, jj)):
			return

		target = 'XMAS'[str_i]
		letter = matrix[ii][jj]
		if letter == target:
			if str_i == 3:
				global part1
				part1 += 1
				return

			scan((ii, jj), offset, str_i + 1)

part1 = 0
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j] != 'X':
			continue

		offsets = list(product([-1, 0, 1], [-1, 0, 1]))
		offsets.remove((0,0))

		for offset in offsets:
			scan((i, j), offset, 1)

part2 = 0
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j] != 'A':
			continue

		offsets = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

		chars = []
		for offset in offsets:
			di, dj = offset
			ii = i + di
			jj = j + dj

			if not in_bounds((ii, jj)):
				break

			chars.append(matrix[ii][jj])

		if chars.count('S') == 2 and chars.count('M') == 2 and chars[0] != chars[2]:
			part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

