from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 100:
        return n ** 2
    if n % 2 == 0:
        return .5 * F(n - 1)
    return 2 * F(n - 1)

for i in range(16385):
    F(i)

print(1000 * F(16384) // F(7777))