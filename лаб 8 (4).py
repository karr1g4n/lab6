import numpy as np

mas = []
for i in range(3):
    d = []
    for j in range(3):
        d.append(int(input("введите первую матрицу по елементно:")))
    mas.append(d)
for k in range(len(mas)):
    s = np.array(mas)
    x = s[::-1]
print(x)
