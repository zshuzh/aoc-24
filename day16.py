from collections import defaultdict
import sys

with open('input.txt', 'r') as f:  
        matrix = [list(line) for line in f.read().splitlines()]

OFFSETS = [(1,0), (0, 1), (-1, 0), (0, -1)]

def clockwise(pos):
    i, j, di, dj = pos
    return (i, j, dj, -di)

def counterclockwise(pos):
    i, j, di, dj = pos
    return (i, j, -dj, di)

def forward(pos):
    i, j, di, dj = pos
    return (i+di, j+dj, di, dj)

def back(pos):
    i, j, di, dj = pos
    return (i-di, j-dj, di, dj)

def valid(pos, rotated):
    i, j, di, dj = pos

    if matrix[i][j] == '#':
        return False

    if rotated and matrix[i+di][j+dj] == '#':
        return False

    return True

start = ()
end = ()
offset = OFFSETS[1]
for i, row in enumerate(matrix):
    for j, el in enumerate(row):
        if el == 'S':
            start = (i,j)
        if el == 'E':
            end = (i,j)

scores = defaultdict(lambda: sys.maxsize)
init = (*start, *offset)
scores[init] = 0

while True:
    s = scores.copy()
    for pos, score in s.items():
        m = forward(pos)
        if valid(m, False) and score + 1 < scores[m]:
            scores[m] = score + 1

        c = clockwise(pos)
        if valid(c, True) and score + 1000 < scores[c]:
            scores[c] = score + 1000

        cc = counterclockwise(pos)
        if valid(cc, True) and score + 1000 < scores[cc]:
            scores[cc] = score + 1000

    if s == scores:
        break

ends = [(*end,di,dj) for di,dj in OFFSETS]

part1 = min([scores[pos] for pos in ends])
print(f"Part 1: {part1}")

positions = set([pos for pos in ends if scores[pos] == part1])
while True:
    s = positions.copy()
    for pos in s:
        score = scores[pos]

        m = back(pos)
        if scores[m] == score - 1:
            positions.add(m)

        c = clockwise(pos)
        if scores[c] == score - 1000:
            positions.add(c)

        cc = counterclockwise(pos)
        if scores[cc] == score - 1000:
            positions.add(cc)

    if s == positions:
        break

seats = set([(i,j) for i,j,*_ in positions])

part2 = len(seats)
print(f"Part 2: {part2}")

