from fnmatch import fnmatch

for i in range(2902302310 - 2902302310 % 1984, 10**10, 1984):
    if fnmatch(str(i), '[2468]9?23?*23[13579][02468]'):
        print(i, i // 1984)