from copy import deepcopy

with open('input.txt', 'r') as f:  
        matrix = f.read().splitlines()

def in_bounds(coord):
        i, j = coord

        if i < 0 or i >= len(matrix):
                return False
        if j < 0 or j >= len(matrix[0]):
                return False

        return True

def count(matrix):
    ret = 0
    for row in matrix:
        for el in row:
            if el == '#':
                ret += 1

    return ret

antinodes = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
harmonics = deepcopy(antinodes)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        e = matrix[i][j] 
        if e == '.':
            continue

        for ii in range(len(matrix)):
            for jj in range(len(matrix[0])):
                if i == ii and j == jj:
                    continue

                ee = matrix[ii][jj]
                if ee != e:
                    continue

                di = ii - i
                dj = jj - j

                iii = ii + di
                jjj = jj + dj
                if in_bounds((iii,jjj)):
                    antinodes[iii][jjj] = '#'

                iii = ii
                jjj = jj
                while in_bounds((iii,jjj)):
                    harmonics[iii][jjj] = '#'
                    iii += di
                    jjj += dj

part1 = count(antinodes)
print(f"Part 1: {part1}")

part2 = count(harmonics)
print(f"Part 2: {part2}")

