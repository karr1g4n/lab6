
import random


while True:
    text = "l like my mam."
    flag = input("елси вы хотите , числа были рандомние нажмите <<enter>>'. Для введення вручную нажмите любую клавишу: ")
    if flag == '':
        str_find = ['like', 'i', 'my']
        pattern = random.choice(str_find)
        print(pattern)

    else:
        pattern = input('введите слова: ')

    i = -1
    j = 0
    count = 0
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        count += 2
        while j < len(pattern) and pattern[j] == text[i + j]:
             j += 1
             count += 2
    if j == len(pattern):
        print(f'слова найдены на {i + 1} позиции ')
    else:
        print('слова не найдены ')

    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break