with open('17_14260.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i > 0 and str(i)[-1] == str(i)[-2] and len(str(i)) == 4)
ans = []

for i in range(len(data) - 2):
    nums = data[i:i+3]
    u1 = all(1 for i in nums if len(str(abs(i))) == 3)
    u2 = sum(nums) > minn
    if u1 and u2:
        ans.append(sum(nums))

print(len(ans), max(ans))
#неправильно