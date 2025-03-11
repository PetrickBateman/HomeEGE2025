from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 110:
        return n
    return n + F(n - 1)

for i in range(2026):
    F(i)

print(F(2025) - F(2021))
