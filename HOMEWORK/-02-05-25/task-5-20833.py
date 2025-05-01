def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for n in range(1, 10000):
    r = convert(n, 5)
    if len(r) % 2 == 0:
        r = r[len(r)//2:] + r[:len(r)//2]
    else:
        r = r + str(n % 5)
        r = r[len(r) // 2:] + r[:len(r) // 2]
    r = int(r, 5)
    if r > 50:
        print(n)
        break