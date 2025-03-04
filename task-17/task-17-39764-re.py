with open('17.txt') as file:
    data = [int(i) for i in file]

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    nums = [num1, num2, num3]
    u1 = max(nums) ** 2 == sum([i * i for i in nums]) - max(nums) ** 2
    if u1:
        ans.append(sum(nums))

print(len(ans), max(ans))