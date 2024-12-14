import re
from copy import deepcopy

with open('input.txt', 'r') as f:  
    data = f.read().splitlines()

ROWS = 103
COLS = 101
SECONDS = 100

def in_bounds(robots):
    for robot in robots:
        px, py, *_ = robot

        if px < 0 or px >= COLS or py < 0 or py >= ROWS:
            return False
    
    return True

def display(matrix):
    for row in matrix:
        s = []
        for el in row:
            if el == 0:
                s.append('.')
            else:
                s.append(str(el))

        print(''.join(s))

def wrap(px, py):
    while px >= ROWS:
        px -= ROWS

    while py >= COLS:
        py -= COLS

    while px < 0:
        px += ROWS

    while py < 0:
        py += COLS

    return px, py

def move(robot):
    px, py, vx, vy = robot

    px += vx
    py += vy

    px, py = wrap(px, py)

    return px, py, vx, vy

def place(robots):
    matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for robot in robots:
        px, py, *_ = robot
        matrix[px][py] += 1

    return matrix

def count(quadrant):
    return sum([el for row in quadrant for el in row])

def contiguous(matrix):
    c = []
    for row in matrix:
        max = curr = 0
        for el in row:
            curr = 0 if el == 0 else curr + 1

            if curr > max:
                max = curr

        if max > 1:
            c.append(max)

    return sum(c)

r = []
for line in data:
    py, px, vy, vx = re.findall(r"[+-]?\d+", line)
    py, px, vy, vx = tuple(map(int, (py, px, vy, vx )))

    px, py = wrap(px, py)
    r.append([px, py, vx, vy])

robots = deepcopy(r)
for _ in range(SECONDS):
    for i, robot in enumerate(robots):
        robots[i] = move(robot)

matrix = place(robots)
xm = ROWS // 2
ym = COLS // 2

q1 = [row[ym+1:] for row in matrix[:xm]]
q2 = [row[:ym] for row in matrix[:xm]]
q3 = [row[:ym] for row in matrix[xm+1:]]
q4 = [row[ym+1:] for row in matrix[xm+1:]]

safety = count(q1) * count(q2) * count(q3) * count(q4)

part1 = safety
print(f"Part 1: {part1}")

robots = deepcopy(r)
n = 0
while True:
    matrix = None
    for i, robot in enumerate(robots):
        robots[i] = move(robot)
        matrix = place(robots)

    n += 1

    if (contiguous(matrix) > 100):
        # uncomment to see the tree!
        # display(matrix)
        break

part2 = n
print(f"Part 2: {part2}")

