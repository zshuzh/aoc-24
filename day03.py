import re

with open('input.txt', 'r') as f:  
        data = f.read().strip()

pattern = r'(mul\(\d+,\d+\))'
matches = re.findall(pattern, data)

part1 = 0
for match in matches:
    x, y = match[4:-1].split(',')

    part1 = part1 + int(x) * int(y)

print(f"Part 1: {part1}")

pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
matches = re.findall(pattern, data)

enabled = True
part2 = 0
for match in matches:
    if match == "do()":
        enabled = True
        continue

    if match == "don't()":
        enabled = False
        continue

    if enabled == False:
        continue

    x, y = match[4:-1].split(',')

    part2 = part2 + int(x) * int(y)

print(f"Part 2: {part2}")

