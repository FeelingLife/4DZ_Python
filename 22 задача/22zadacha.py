# Задача 22 - Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества, m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества - "))
m = int(input("Введите кол-во элементов второго множества - "))
array_n = []
array_m = []
for i in range(n):
    array_n.append(int(input("Введите элемент первого массива - ")))
for j in range(m):
    array_m.append(int(input("Введите элемент второго массива - ")))
array_general = []
for i in array_n:
    if i in array_m and i not in array_general:
        array_general.append(i)
array_general.sort()
print(array_general)