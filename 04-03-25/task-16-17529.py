from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    return n * F(n-1)

for i in range(1, 2025):
    F(i)

print((2 * F(2024) + F(2023)) / F(2022))