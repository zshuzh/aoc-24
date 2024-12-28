from collections import defaultdict
from itertools import product, combinations

with open('input.txt', 'r') as f:  
    data = [line.split('-') for line in f.read().splitlines()]

connections = defaultdict(set)

for c1,c2 in data:
    connections[c1].add(c2)
    connections[c2].add(c1)

triples = set()
for c1, c in connections.items():
    for c2,c3 in product(c,c):
        if c2 == c3:
            continue

        if c2 in connections[c3]:
            triples.add(frozenset([c1,c2,c3]))

part1 = len([c for c in triples if any([c.startswith('t') for c in c])])
print(f"Part 1: {part1}")

computers = set([c for connection in data for c in connection])

cliques = triples
while len(cliques) != 1:
    next = set()

    for clique in cliques:
        for c in computers:
            comps = list(clique) + [c]

            valid = True
            for combo in combinations(comps, len(comps) - 1):
                if frozenset(combo) not in cliques:
                    valid = False
                    break

            if valid:
                next.add(frozenset(comps))

    cliques = next

part2 = ','.join(sorted(list(cliques)[0]))
print(f"Part 2: {part2}")

