with open('17_19249.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if len(str(i)) == 5  and str(i)[-2:] == '43'])
ans = []

for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    nums = [num1, num2, num3]
    u1 = sum([1 for i in nums if len(str(abs(i))) == 5 and str(i)[-2:] == '43']) != 0
    u2 = maxx ** 2 >= sum(i * i for i in nums)
    if u1 and u2:
        ans.append(sum(i * i for i in nums))

print(len(ans), min(ans))