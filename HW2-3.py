# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

n = int(input("Введите значение: "))
result =0
for i in range (1, n+1):
    result += (1+(1/i))**i
print(result)