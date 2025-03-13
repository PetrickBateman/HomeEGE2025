from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 11:
        return n
    if n % 2 == 0:
        return 2 * n - 3 + F(n - 2)
    else:
        return 3 * n - 4 + F(n - 3)

for i in range(5501):
    F(i)

print(F(5500) - F(5497))