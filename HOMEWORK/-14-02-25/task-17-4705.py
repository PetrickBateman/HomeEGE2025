with open('17_4705.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if str(i)[-1:] == '3'])
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    nums = [num1, num2]
    u1 = sum([1 for i in nums if str(i)[-1:] == '3']) == 1
    u2 = maxx ** 2 <= sum([i*i for i in nums])
    if u1 and u2:
        ans.append(sum([i*i for i in nums]))

print(len(ans), max(ans))