from fnmatch import fnmatch

def f(n):
    res = set()
    for i in range(2, int(n ** .5)):
        if n % i == 0:
            res |= {i, n // i}
    if sum(1 for i in res if fnmatch(str(i), '4*')) == 24:
        res1 = set()
        for j in res:
            for l in range(2, int(j ** .5)):
                if j % l == 0:
                    res1 |= {l, j // l}
        if fnmatch(str(max(res1)), '4*'):
            return max(res)
        return 0
    return 0

for i in range(1, 10**6):
    f = f(i)
    if f:
        print(i, f)
