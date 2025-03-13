def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (x >= 11) or ((3 * x) < y) or ((x * y) < A)
            if u:
                return A
    return 0

for A in range(1, 1000):
    if f(A):
        print(A)
        break