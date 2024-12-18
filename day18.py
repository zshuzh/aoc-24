from collections import defaultdict
import sys

with open('input.txt', 'r') as f:  
    data = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

SIZE = 70 + 1
ITER = 1024
OFFSETS = [(1,0), (0, 1), (-1, 0), (0, -1)]

map = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

def in_bounds(coord):
        i, j = coord

        if i < 0 or i >= len(map):
                return False
        if j < 0 or j >= len(map[0]):
                return False

        return True

def scan(start):
    scores = defaultdict(lambda: sys.maxsize, { start: 0 })
    u = [start]
    uu = []
    while True:
        for c in u:
            for o in OFFSETS:
                i, j = c
                di, dj = o

                ii = i + di
                jj = j + dj
                cc = (ii,jj)

                if not in_bounds(cc):
                    continue

                if map[ii][jj] == '#':
                    continue

                if scores[c] + 1 < scores[cc]:
                    scores[cc] = scores[c] + 1
                    uu.append(cc)

        if not uu:
            return scores
        else:
            u = uu
            uu = []

for i in range(ITER):
    j,i = data[i]
    map[i][j] = '#'

start = (0,0)
end = (SIZE-1,SIZE-1)

part1 = scan(start)[end]
print(f"Part 1: {part1}")

coord = (None, None)
for n in range(ITER, len(data)):
    j,i = data[n]
    map[i][j] = '#'

    if scan(start)[end] == sys.maxsize:
        coord = data[n]
        break

i,j = coord
part2 = ','.join([str(i),str(j)])
print(f"Part 2: {part2}")

