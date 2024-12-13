from collections import defaultdict

with open('input.txt', 'r') as f:  
        data = [int(ch) for ch in f.read().strip().split(' ')]

def slow(iter):
    s = data[:]
    ss = []
    for _ in range(iter):
        for stone in s:
            if stone == 0:
                ss.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = str(stone)[:mid]
                right = str(stone)[mid:]
                ss += [int(left), int(right)]
            else:
                ss.append(stone * 2024)

        s = ss
        ss = []

    return len(s)

def fast(iter):
    s = defaultdict(int, {k: 1 for k in data})
    for _ in range(iter):
        ss = defaultdict(int)
        ss[1] = s[0]
        for stone, count in s.items():
            if stone == 0:
                continue
            
            if len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = str(stone)[:mid]
                right = str(stone)[mid:]
                ss[int(left)] += count 
                ss[int(right)] += count
            else:
                ss[stone * 2024] += count

        s = ss

    return sum(s.values())

part1 = slow(25)
print(f"Part 1: {part1}")

part2 = fast(75)
print(f"Part 2: {part2}")

