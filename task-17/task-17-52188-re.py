with open('17.txt') as file:
    data = [int(i) for i in file]

minn = min([i for i in data if str(i)[-1] == '3']) ** 2
ans = []

for i in range(len(data) - 1):
    nums = data[i:i+2]
    u1 = str(min(nums))[-1] == '3'
    u2 = sum([i * i for i in nums]) < minn
    if u1 and u2:
        ans.append(sum([i * i for i in nums]))

print(len(ans), max(ans))