# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input("Введите значение: "))
list = []
for i in range(n):
    list.append(random.randint(-n, n))
print(list)

# код для создания файла и передачи в него данных:
data = open('file.txt', 'w')
data.write('2\n') # "\n" - перенос строки
data.write('3')
result = 1
data = open('file.txt', 'r')
for line in data:
    print(line)
    result = result*list[int(line)]
data.close()
print(result)

# вариант2 : Ввод индексов пользователем
# import random
# n = int(input("Введите значение: "))
# # poz1 = int(input("Введите значение позиции 1: "))
# # poz2 = int(input("Введите значение позиции 2: "))
# list = []
# for i in range(n):
#     list.append(random.randint(-n, n))
# print(list)
# if poz1 & poz2 in range (-n, n):
#     result = list[poz1]*list[poz2]
#     print(f'Произведение заданных элементов массива: {result}')
# else: print("Ведите позиции в диапазоне 0:n")

# with open('file.txt', 'r') as data:
#     for line in data:
#         var = data.readline
#         print(var)

# Вывод элементов масссива от - n до  n
# result =1
# lst = []
# for i in range(-n, n+1):
#     result=i
#     lst.append(result)
# print(lst)
