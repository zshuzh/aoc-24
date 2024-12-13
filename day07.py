import re
from itertools import product

with open('input.txt', 'r') as f:  
        data = f.read().splitlines()

def evaluate(exp):
    ret = int(exp[0])
    
    for i in range(1, len(exp), 2):
        op = exp[i]
        n = int(exp[i+1])

        if op == '+':
            ret += n
        elif op == '*':
            ret *= n
        elif op == '||':
            ret = int(str(ret) + str(n))

    return ret

def calibrate(operations):
    ret = 0
    for line in data:
        matches = re.findall(r"\d+", line)

        sum = int(matches[0])
        operands = matches[1:]
        ops_perms = list(product(operations, repeat=len(operands)-1))
        
        for ops in ops_perms:
            exp = [item for pair in zip(operands, ops) for item in pair] + [operands[-1]]
            if evaluate(exp) == sum:
                ret += sum
                break

    return ret

part1 = calibrate(['+', '*'])
print(f"Part 1: {part1}")

part2 = calibrate(['+', '*', '||'])
print(f"Part 2: {part2}")

