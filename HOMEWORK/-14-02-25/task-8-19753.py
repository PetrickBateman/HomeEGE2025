from itertools import permutations

ch = '02468'
nch = '13579'
count = 0
for p in permutations('0123456789', 6):
    p = ''.join(p)
    if p[0] != '0' and int(p) % 4 == 0:
        for i in p:
            if i in ch:
                p = p.replace(i, '*')
        if '**' not in p:
            count += 1

print(count)