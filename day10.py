with open('input.txt', 'r') as f:  
        matrix = [list(map(int, list(line))) for line in f.read().splitlines()]

def in_bounds(coord):
        i, j = coord

        if i < 0 or i >= len(matrix):
                return False
        if j < 0 or j >= len(matrix[0]):
                return False

        return True

def score(trails):
    s = set()
    for trail in trails:
        s.add((trail[0], trail[-1]))

    return len(s)

trailheads = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            trailheads.append([(i,j)])

t = trailheads
tt = []
for _ in range(9):
    for trail in t:
        coord = trail[-1]
        steps = len(trail)

        for offset in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            i, j = coord
            di, dj = offset

            ii = i + di
            jj = j + dj

            if in_bounds((ii,jj)) and matrix[ii][jj] == steps:
                tt.append([*trail, (ii,jj)])
    
    t = tt
    tt = []

part1 = score(t)
print(f"Part 1: {part1}")

part2 = len(t)
print(f"Part 2: {part2}")

