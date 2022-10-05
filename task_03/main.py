# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
number = int(input('Введите размер списка : '))
def FromDecimalToBinary (num):
    count = 0
    res = 0
    flag = True
    if num < 0:
        num = abs(num)
        flag = False
    while num > 0:
        res += (num % 2) * 10 ** count
        num = num // 2
        count+=1
    return -res if flag == False else res
print(FromDecimalToBinary(number))