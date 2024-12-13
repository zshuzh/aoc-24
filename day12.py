from collections import Counter

with open('input.txt', 'r') as f:  
        matrix = [list(line) for line in f.read().splitlines()]

OFFSETS = [(1,0), (0, 1), (-1, 0), (0, -1)]

def in_bounds(coord):
        i, j = coord

        if i < 0 or i >= len(matrix):
                return False
        if j < 0 or j >= len(matrix[0]):
                return False

        return True

def add_tuples(x, y):
    return tuple(a + b for a, b in zip(x, y))

def area(region):
    return len(region)

def perimeter(region):
    ret = 0

    for coord in region:
        for offset in OFFSETS:
            i, j = coord
            di, dj = offset

            ii = i + di
            jj = j + dj

            if (ii,jj) not in region:
                ret += 1

    return ret

def edges(region):
    internal = []
    external = []

    for coord in region:
        for offset in OFFSETS:
            i, j = coord
            di, dj = offset

            ii = i + di
            jj = j + dj

            if (ii,jj) not in region:
                internal.append([coord, offset])
                external.append([(ii,jj),(-di,-dj)])

    return internal, external

def corners(edges):
    ret = []
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            if i == j:
                continue

            ci, oi = edges[i]
            cj, oj = edges[j]

            diagonal = add_tuples(oi,oj)
            if ci == cj and diagonal != (0,0):
                x,y = ci
                if diagonal == (-1,-1):
                    ret.append((x,y))
                elif diagonal == (-1,1):
                    ret.append((x,y+1))
                elif diagonal == (1,-1):
                    ret.append((x+1,y))
                elif diagonal == (1,1):
                    ret.append((x+1,y+1))

    return ret

def sides(region):
    internal, external = edges(region)

    corns = corners(internal) + corners(external)

    sides = 0
    for count in Counter(corns).values():
        if count > 1:
            sides += 2
        else:
            sides += 1

    return sides

regions = []
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if (x,y) in [coord for region in regions for coord in region]:
            continue

        region = [(x,y)]
        while True:
            grew = False
            for coord in region:
                for offset in OFFSETS:
                    i, j = coord
                    di, dj = offset

                    ii = i + di
                    jj = j + dj

                    if (ii,jj) in region:
                        continue
                    if not in_bounds((ii,jj)):
                        continue
                    if matrix[i][j] != matrix[ii][jj]:
                        continue

                    region.append((ii,jj))
                    grew = True

            if not grew:
                break

        regions.append(region)

part1 = sum([area(region) * perimeter(region) for region in regions])
print(f"Part 1: {part1}")

part2 = sum([area(region) * sides(region) for region in regions])
print(f"Part 2: {part2}")

