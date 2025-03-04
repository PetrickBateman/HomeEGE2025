def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 1001):
    r = convert(n, 7)
    if n % 2 == 0:
        r = '52' + r + '1'
    else:
        r = r[-1] + r[1:-1] + r[0] + '15'
    for i in range(len(r)):
        if r[0] == '0':
            r = r[1:]
        if len(r) == 4:
            ans.append(n)
print(max(ans))