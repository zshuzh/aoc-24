from copy import deepcopy

with open('input.txt', 'r') as f:  
        data = [list(line) for line in f.read().splitlines()]

def in_bounds(coord):
	i, j = coord

	if i < 0 or i >= len(matrix):
		return False
	if j < 0 or j >= len(matrix[0]):
		return False

	return True

def rotate(offset):
    (i, j) = offset
    return (j, -i)

def move(coord, offset):
    i, j = coord
    di, dj = offset

    ii = i + di
    jj = j + dj

    if not in_bounds((ii, jj)):
        return (None, offset)

    if matrix[ii][jj] == '#':
        return (coord, rotate(offset))
    else:
        matrix[ii][jj] = 'X'
        return ((ii,jj), offset)

def start():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^':
                matrix[i][j] = 'X'
                return (i,j)

def count():
    ret = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'X':
                ret += 1

    return ret

matrix = deepcopy(data)
coord = start()
offset = (-1, 0)
while(True):
    coord, offset = move(coord, offset)

    if not coord:
        break

part1 = count()
print(f"Part 1: {part1}")

loops = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix = deepcopy(data)
        coord = start()
        offset = (-1, 0)
        visited = set()

        if matrix[i][j] == '#' or (i,j) == start:
            continue
        else:
            matrix[i][j] = '#'

        while(True):
            visited.add((coord, offset))

            coord, offset = move(coord, offset)

            if (coord, offset) in visited:
                loops += 1
                break

            if not coord:
                break

part2 = loops
print(f"Part 2: {part2}")

