from fnmatch import fnmatch
from itertools import product

def prime(N):
    for i in range(2, int(N ** .5) + 1):
        if N % i == 0:
            return N
    return 0

ans = []
for g in range(4):
    for r in range(4):
        for R in range(4 - r):
            for N in product('0123456789', repeat=g):
                for x in product('0123456789', repeat=r):
                    for X in product('0123456789', repeat=R):
                        x = ''.join(x)
                        X = ''.join(X)
                        N = ''.join(N)
                        N = int(N)
                        if prime(N):
                            num = int(f'1{N}03{x}6{X}')
                            if num < 10 ** 8 and num % 22768 == 0:
                                ans.append([num, N])
ans = sorted(ans)
for i in ans:
    print(*i)