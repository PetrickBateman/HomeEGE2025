from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 11:
        return n
    return n + F(n - 1)

for i in range(10, 2025):
    F(i)

print(F(2024) - F(2021))