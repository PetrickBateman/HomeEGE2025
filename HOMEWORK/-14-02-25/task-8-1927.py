from itertools import product

alph = sorted(set('ЯСНОВИДЕЦ'))
sogl = 'СНВДЦ'
count = 0

for p in product(alph, repeat=5):
    p = ''.join(p)
    if p[0] in sogl and p[-1] not in sogl:
        if p.count(p[0]) + p.count(p[-1]) == 2:
            count += 1

print(count)