'''Определить индексы элементов массива (списка),значения которых принадлежат заданному
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]'''
len = int(input("Введите размер массива: "))
from random import randint
list = [randint(-10,10) for i in range(len)]
print(list)
lenmin = int(input("Введите минимум: "))
lenmax = int(input("Введите максимум: "))
lstIndex = []
for i in range(len):
    if lenmin <= list[i] <= lenmax:
        lstIndex.append(i)
print(lstIndex)