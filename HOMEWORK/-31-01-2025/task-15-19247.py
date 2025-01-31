def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - 3 * y < A) or (y > 400) or (x > 56)
            if not f:
                return False
    return True
for A in range(1, 10000):
    if f(A):
        print(A)
        break