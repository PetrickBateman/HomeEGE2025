def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

l = []
for n in range(1, 10000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + convert(sum(map(int, r)), 3)
    r = int(r, 3)
    if r > 220 and r % 2 == 0:
        l.append(r)
print(min(l))