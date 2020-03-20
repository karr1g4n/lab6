import numpy as np
import random
while True:

    g = input("елси вы хотите , числа были рандомние нажмите <<enter>>'. Для введення вручную нажмите любую клавишу: ")
#вибираємо як буде проходити пошук
    a = np.zeros(10, dtype=int)
    while True:
        try:
            x = int(input('введите искамое число: '))#вводимо число яке будемо шукати
            break
        except ValueError:
            print("только числа")
    n = len(a)

    if g== '':
        while True:
            try:
                q1 =int(input("Введите левую границу: "))
                q2=int(input("введите правую гаринц: "))
                break
            except ValueError:
                print("только цифри")

        for i in range(10):
            a[i] = random.randint(q1, q2)
    else:
        for i in range(10):
            a[i] = int(input(f'Enter {i + 1} element: '))
    print(a)

    a = sorted(a)#сортуємо наш масив
    print(a)
    l = 0
    r = len(a) - 1
    k = 0
    count = 0
    flag = False
    while l <= r and not flag: #робимо як було в прикладі
        count += 2
        k = (l + r) // 2
        if a[k] == x:
            flag = True

        elif a[k] < x:
            count += 1
            l = k + 1
        else:
            count += 1
            r = k - 1
    if not flag:
        print('ЕЛЕМЕНТ НЕ НАЙДЕН')
    else:
        print(f'елемнт найден{x} на {k + 1} позици ')
    print(f"Сравнения были выполнены{count} ")
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
