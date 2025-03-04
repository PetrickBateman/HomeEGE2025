def f(num):
    res = set()
    for i in range(int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    if len(res) >= 11:
        if sum(res) % 2 == 0 and sum([1 * i for i in res]) % 2 == 0:
            return len(res)