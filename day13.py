import re

with open('input.txt', 'r') as f:  
        rules = [block.splitlines() for block in f.read().split('\n\n')]

def slow(ax, ay, bx, by, px, py):
    a = 0
    while True:
        tx = px - a * ax
        ty = py - a * ay

        if tx < 0 or ty < 0:
            break

        if tx % bx == 0 and ty % by == 0 and tx // bx == ty // by:
            b = tx // bx
            return 3 * a + b 
        a += 1

    return None

def fast(ax, ay, bx, by, px, py):
    am = ay / ax
    bm = by / bx

    ix = (py - bm * px) / (am - bm)

    a = round(ix / ax)
    b = (px - a * ax) // bx

    if (a * ax + b * bx, a * ay + b * by) == (px, py):
        return 3 * a + b 
    else:
        return None

part1 = 0
part2 = 0
for rule in rules:
    ax, ay = re.findall(r"\d+", rule[0])
    bx, by = re.findall(r"\d+", rule[1])
    px, py = re.findall(r"\d+", rule[2])

    ax, ay, bx, by, px, py = tuple(map(int, (ax, ay, bx, by, px, py)))

    tokens = slow(ax, ay, bx, by, px, py)
    if tokens:
        part1 += tokens

    tokens = fast(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
    if tokens:
        part2 += tokens

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

