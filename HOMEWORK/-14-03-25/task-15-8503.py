def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (x & 52 != 0) and (x & 36 == 0) <= (not(x & A == 0))
            if u:
                return A
    return 0

for A in range(1, 1000):
    w = f(A)
    if w:
        print(A)
        break