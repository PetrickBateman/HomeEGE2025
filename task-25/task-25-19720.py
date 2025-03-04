from itertools import product

ans = []
for r in range(3):
    for R in range(3 - r):
        for x in product('13579', repeat=r):
            for X in product('13579', repeat=R):
                for y in '02468':
                    x = ''.join(x)
                    X = ''.join(X)
                    num = int(f'1{x}2{y}3{X}45')
                    if num < 10 ** 8 and num % 153 == 0:
                        ans.append((num, num // 153))

ans = sorted(ans)
for i in ans:
    print(*i)