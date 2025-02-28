from itertools import product

ans = []
for r in range(4):
    for x in product('0123456789', repeat=r):
        for y in '0123456789':
            x = ''.join(x)
            num = int(f'{y}2139{x}4')
            if num < 10 ** 10 and num % 3052 == 0:
                ans.append([num, num // 3052])
ans = sorted(ans)
for i in ans:
    print(*i)