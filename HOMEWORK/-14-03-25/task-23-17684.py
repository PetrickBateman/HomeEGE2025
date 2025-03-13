def f(cur, end):
    if cur == end:
        return 1
    if cur < 2:
        return 0
    return f(cur - 2, end) + f(cur // 2, end)

print(f(38, 10) * f(10, 2))