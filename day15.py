from copy import deepcopy

with open('input.txt', 'r') as f:  
    _map, _moves = f.read().split('\n\n')
    map = [list(line) for line in _map.splitlines()]
    moves = ''.join(_moves.splitlines())

MOVES = { ">": (0,1), "<": (0, -1), "^": (-1, 0), "v": (1, 0) }

def move(coord, delta, map):
    iters = [[coord]]
    done = { coord }

    while True:
        iter = []
        for c in iters[-1]:
            i,j = c
            di,dj = delta
            ii,jj = i+di,j+dj

            if map[ii][jj] == '#':
                return coord, map
            if map[ii][jj] == '.':
                continue
            if map[ii][jj] == 'O':
                iter.append((ii,jj))
                done.add((ii,jj))
            if map[ii][jj] == '[':
                l = (ii,jj) 
                r = (ii,jj+1)
                if l not in done:
                    iter.append(l)
                    done.add(l)
                if r not in done:
                    iter.append(r) 
                    done.add(r)
            if map[ii][jj] == ']':
                l = (ii,jj-1) 
                r = (ii,jj)
                if r not in done:
                    iter.append(r)
                    done.add(r)
                if l not in done:
                    iter.append(l) 
                    done.add(l)

        if len(iter) == 0:
            break
        else:
            iters.append(iter)

    m = deepcopy(map)
    coords = [item for iter in iters for item in iter][::-1]
    for c in coords:
        i,j = c
        di,dj = delta
        ii,jj = i+di,j+dj
        m[ii][jj] = m[i][j]
        m[i][j] = '.'

    i,j = coord
    di,dj = delta
    ii,jj = i+di,j+dj

    return (ii,jj), m

def gps(map):
    ret = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'O' or map[i][j] == '[':
                ret += 100 * i + j

    return ret

def start(map):
    ret = (0,0)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                ret = (i,j)

    return ret

megamap = [[] for _ in range(len(map))]
for i in range(len(map)):
    for j in range(len(map[0])):
        el = map[i][j] 
        if el == '.' or el == '#':
            megamap[i].append(el)
            megamap[i].append(el)
        if el == 'O':
            megamap[i].append('[')
            megamap[i].append(']')
        if el == '@':
            megamap[i].append('@')
            megamap[i].append('.')

coord = start(map)
for m in moves:
    delta = MOVES[m]
    coord, map = move(coord, delta, map)

coord = start(megamap)
for m in moves:
    delta = MOVES[m]
    coord, megamap = move(coord, delta, megamap)

part1 = gps(map)
print(f"Part 1: {part1}")

part2 = gps(megamap)
print(f"Part 2: {part2}")

