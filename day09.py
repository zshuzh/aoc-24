from copy import deepcopy

with open('input.txt', 'r') as f:  
        data = f.read().strip()

def checksum(disk):
    ret = 0
    for i, ch in enumerate(disk):
        if ch != '.':
            ret += i * int(ch)

    return ret

disk = []
for i, ch in enumerate(data):
    if i % 2 == 0:
        disk += [i//2 for _ in range(int(ch))]
    else:
        disk += ['.' for _ in range(int(ch))]

d = deepcopy(disk)
marker = 0
for i in range(len(d)-1, -1, -1):
    if d[i] == '.':
        continue

    for j in range(marker, len(d)):
        if j < i and d[j] == '.':
            d[i], d[j] = d[j], d[i]
            marker = j + 1
            break

part1 = checksum(d)
print(f"Part 1: {part1}")

d = deepcopy(disk)
file = len(data) // 2
length = 1
for i in range(len(d)-1, -1, -1):
    if d[i] != file:
        continue

    if d[i-1] == file:
        length += 1
        continue

    for j in range(len(d)):
        if j < i and d[j:j+length] == ['.'] * length:
            d[i:i+length], d[j:j+length] = d[j:j+length], d[i:i+length]
            break

    length = 1
    file -= 1

part2 = checksum(d)
print(f"Part 2: {part2}")

