def prime(num):
    if num >= 2:
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                return 0
        return num
    return 0

def div(num):
    res = set()
    for i in range(2, int(num * .5) + 1):
        if prime(num):
            return 0
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) >= 2:
        M = sum(res)
        if prime(M % 100_000):
            return M
        return 0

count = 0
for i in range(1_273_548, 10**20):
    res = div(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break