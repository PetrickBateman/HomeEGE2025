def div(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) >= 2:
        M = min(res) + max(res)
        if M % 10 == 4:
            return M
        return 0
    return 0

count = 0
for i in range(220_001, 10 ** 20):
    res = div(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break