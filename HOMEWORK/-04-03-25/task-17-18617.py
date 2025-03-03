with open('17_18617.txt') as file:
    data = [int(i) for i in file]

maxx = max(data) % 3
minn = min(data) % 7
ans = []

for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    nums = [num1, num2]
    u1 = [1 for i in nums if i % 3 == maxx]
    u2 = [1 for i in nums if i % 7 == minn]
    if u1 and u2:
        ans.append(sum(nums))

print(len(ans), max(ans))