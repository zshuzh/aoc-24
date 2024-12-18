import re

with open('input.txt', 'r') as f:  
    _r, _p = f.read().split('\n\n')
    r = [int(n) for n in re.findall(r"\d+", _r)]
    p = [int(n) for n in re.findall(r"\d+", _p)]

def combo(o,a,b,c):
    match o:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case _:
            return o

def run(r,p):
    ip = 0
    a,b,c = r
    ret = []
    while(True):
        i = p[ip]
        o = p[ip+1]

        match i:
            case 0:
                a = int(a / 2 ** combo(o,a,b,c))
            case 1:
                b = b ^ o
            case 2:
                b = combo(o,a,b,c) % 8
            case 3:
                if a != 0:
                    ip = 0
                    continue
            case 4:
                b = b ^ c
            case 5:
                ret.append(combo(o,a,b,c) % 8) 
            case 6:
                b = int(a / 2 ** combo(o,a,b,c))
            case 7:
                c = int(a / 2 ** combo(o,a,b,c))

        ip += 2
        if ip >= len(p):
            break

    return ret

part1 = ','.join([str(n) for n in run(r,p)])
print(f"Part 1: {part1}")

def compatible(b, bb):
    for x, y in zip(b, bb):
        if x is not None and x != y:
            return False

    return True

def itob(n):
    return [int(n) for n in str(format(n, '03b'))]

def otoi(o):
    oo = [str(n) for n in o]
    return int(''.join(oo), 8)

def end(s):
    return s + 3 if s + 3 != 0 else None

ob = { (): [0] * 8 + [None] * (len(p) * 3) }
for i in range(len(p)):
    obob = ob.copy()
    ob = {}
    for o, b in obob.items():
        for n in range(8):
            bb = b.copy()
            s = -3 * (i+1)
            bb[s:end(s)] = itob(n)

            if not compatible(b, bb):
                continue

            s = s - (n ^ 5)
            bbb = bb.copy()
            bbb[s:end(s)] = itob(n ^ 5 ^ 6 ^ p[i])

            if not compatible(bb, bbb):
                continue

            oo = (n,) + o
            ob[oo] = bbb

part2 = min([otoi(o) for o in ob.keys()])
print(f"Part 2: {part2}")

