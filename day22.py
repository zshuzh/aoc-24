from collections import defaultdict

with open('input.txt', 'r') as f:  
    data = [int(line) for line in f.read().splitlines()]

def mix(secret, number):
    return secret ^ number

def prune(secret):
    return secret % 16777216

def generate(s):
    s = mix(s, s * 64)
    s = prune(s)

    s = mix(s, s // 32)
    s = prune(s)

    s = mix(s, s * 2048)
    s = prune(s)

    return s

secrets = []
for s in data:
    for _ in range(2000):
        s = generate(s)

    secrets.append(s)

bananas = defaultdict(int)
for s in data:
    ones = []
    for _ in range(2000):
        s = generate(s)
        ones.append(s % 10)

    changes = [None]
    for i in range(1, len(ones)):
        changes.append(ones[i] - ones[i-1])

    done = set()
    for i in range(4, len(ones)):
        val = ones[i]
        key = tuple(changes[i-3:i+1])

        if key not in done:
            bananas[key] += val
            done.add(key)

part1 = sum(secrets)
print(f"Part 1: {part1}")

part2 =  max(bananas.values())
print(f"Part 2: {part2}")

