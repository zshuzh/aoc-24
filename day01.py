from collections import Counter

with open('input.txt', 'r') as f:  
	data = [line.split() for line in f.read().splitlines()]

l = []
r = []

for x,y in data:
    l.append(int(x))
    r.append(int(y))

ll = sorted(l)
rr = sorted(r)

distances = []
for i in range(len(l)):
    distances.append(abs(ll[i] - rr[i]))

part1 = sum(distances)
print(f"Part 1: {part1}")

count = Counter(r)

sims = []
for el in l:
    sims.append(int(el) * int(count[el]))

part2 = sum(sims)
print(f"Part 2: {part2}")

