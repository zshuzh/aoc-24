with open('input.txt', 'r') as f:  
        rules, updates = f.read().split('\n\n')
        rules = [list(map(int, line.split('|'))) for line in rules.splitlines()]
        updates = [list(map(int, line.split(','))) for line in updates.splitlines()]

def rindex(list, el):
    try:
        i = list[::-1].index(el)
        return len(list) - 1 - i
    except ValueError:
        return 0

def validate(pages, rule):
    first, second = rule

    f = rindex(pages, first)
    if (second in pages[:f]):
        return False

    return True

def fix(pages, rule):
    first, second = rule

    f = rindex(pages, first)
    s = pages.index(second)

    element = pages.pop(f)
    pages.insert(s, element)

valid_pages = []
invalid_pages = []
for pages in updates:
    valid = True
    for rule in rules:
        if not validate(pages, rule):
            valid = False
            break
    
    if valid:
        valid_pages.append(pages)
    else:
        invalid_pages.append(pages)

part1 = 0
for pages in valid_pages:
    part1 += pages[len(pages) // 2]

for pages in invalid_pages:
    while(True):
        fixed = False
        for rule in rules:
            if not validate(pages, rule):
                fix(pages, rule)
                fixed = True

        if not fixed:
            break

part2 = 0
for pages in invalid_pages:
    part2 += pages[len(pages) // 2]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

