# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
from math import ceil, floor
from random import sample
number = int(input('Введите размер списка : '))
def MyltiplyOfPairs (num):
    arr = sample(range(0,num**2),num)
    res = []
    print(arr)
    for i in range(floor(num/2)):
        res.append(arr[i] * arr[-(i+1)])
    if num % 2 == 1:
        res.append(arr[ceil(num/2)-1])
    print(res)
MyltiplyOfPairs(number)