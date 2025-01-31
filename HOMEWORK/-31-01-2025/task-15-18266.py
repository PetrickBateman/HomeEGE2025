def f(A):
    for x in range(1, 1000):
        f = (x & 57 == 0) or ((x & 23 == 0) <= (not x & A == 0))
        if not f:
            return False
    return True

for A in  range(1, 10000):
    if f(A):
        print(A)
        break