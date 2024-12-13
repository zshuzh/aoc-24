with open('input.txt', 'r') as f:  
	data = f.read().splitlines()

def is_safe(nums):
	diffs = []
	for i in range(1, len(nums)):
		diffs.append(nums[i] - nums[i-1])

	safe = True
	for i in range(len(diffs)):
		d = diffs[i]

		if abs(d) < 1 or abs(d) > 3:
			safe = False

		if i == 0:
			continue

		dd = diffs[i-1]
		if d < 0 < dd or dd < 0 < d:
			safe = False

	return safe

part1 = 0
for line in data:
	nums = [int(el) for el in line.split(' ')]
	if is_safe(nums):
		part1 = part1 + 1

print(f"Part 1: {part1}")

part2 = 0
for line in data:
	nums = [int(el) for el in line.split(' ')]

	if is_safe(nums):
		part2 = part2 + 1
		continue;

	for i in range(len(nums)):
		if is_safe(nums[:i] + nums[i+1:]):
			part2 = part2 + 1
			break;

print(f"Part 2: {part2}")

