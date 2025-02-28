from itertools import product

ans = []
for r in range(3):
    for R in range(3 - r):
        for x in product('123456789', repeat=r):
            for X in product('0123456789', repeat=R):
                x = ''.join(x)
                X = ''.join(X)
                num = int(f'{x}15{X}7424')
                if num < 10 ** 8:
                    if num % 111 == 0:
                        ans.append([num, num // 111])
                    if num % 113 == 0:
                        ans.append([num, num // 113])
                    if num % 127 == 0:
                        ans.append([num, num // 127])
ans = sorted(ans)
for i in ans:
    print(*i)