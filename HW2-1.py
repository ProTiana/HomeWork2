# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.


n = int(input("Введите значение"))
slovar = {}
for i in range(1, n+1):
    key = i
    value = 3*i+1
    slovar[key]=value
print(f'Словарь:{slovar}')