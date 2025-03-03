def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) >= 3:
            return sum(res[-3:])
    return 0


count = 0
for i in range(2, 1_200_001)[::-1]:
    S = f(i)
    if S:
        if (S % 2022 == 0) and (S != i):
            print(i, S)
            count += 1
            if count == 5:
                break