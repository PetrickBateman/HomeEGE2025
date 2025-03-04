from itertools import combinations

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    f = P <= ((Q <= (not A)) <= (not P))
    if f:
        return True
    return False

ans = []
line = [x % 10 for x in range(15 * 10, 63 * 30)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))