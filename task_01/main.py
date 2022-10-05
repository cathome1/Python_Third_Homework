# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
from random import randint
def SummOfArray (count):
    arr = []
    res = 0
    for i in range(count):
        arr.append(randint(0,count**2))
    print(arr)
    for k in range(0,count+1, 2):
        res+=arr[k]
    print(res)
num = int(input('Введите размер списка : '))
SummOfArray(num)