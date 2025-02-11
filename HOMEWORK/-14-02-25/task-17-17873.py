with open('17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
ans = []

for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    nums = [num1, num2]
    u1 = [1 for i in nums if i % 16 == minn].count(1) != 0
    if u1:
        ans.append(num1 + num2)

print(len(ans), max(ans))