from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n ** 3 + F(n - 1)

for i in range(2026):
    F(i)

print(F(2025) - F(2022))