import numpy as np
import random


g = input("елси вы хотите , числа были рандомние нажмите <<enter>>'. Для введення вручную нажмите любую клавишу: ")

a = np.zeros(10, dtype=int)
x = int(input('елемент который мы ищем: '))
n = len(a)

if g == '':
    q1, q2 = int(input('левая граница: ')), \
             int(input('правая граница: '))
    for i in range(10):
        a[i] = random.randint(q1, q2)
else:
    for i in range(10):
        a[i] = int(input('введите по елементно: '))
print(a)

i = 0
count = 0
while i < n and a[i] != x:
    i += 1
    count += 2
if i == n:
    print('елемент нне найден')
else:
    print(f"елемент {x} найден на {i + 1} позиции")
print(f"сравнювалось{count} раз")
