for p in range(17, 37):
    num1 = int('17496', p)
    num2 = int('91F83', p)
    num3 = int('D9543', p)
    num = num1 + num2 + num3
    if num % 12 == 0:
        print(p, num // 12)