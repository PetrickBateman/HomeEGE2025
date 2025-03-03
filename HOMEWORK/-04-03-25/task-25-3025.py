def div(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    print(res)
    if len(res) >= 6 and res[-6] % 2 != 0:
        return res[-6]
    return 0

count = 0
for i in range(200_000_001, 10 ** 20):
    res = div(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
#неправильно