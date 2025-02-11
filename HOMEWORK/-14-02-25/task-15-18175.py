def f(A):
    for x in range(1, 1000):
        f = ((not x % 7 == 0) and (x % 13 == 0)) <= (x > A - 40)
        if not f:
            return False
    return True

for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break
