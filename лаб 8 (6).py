import numpy as np
a=3
b=3
mas=[]
for i in range(a):
    d=[]
    for j in range(b):
        d.append(int(input("введите первую матрицу по елементно:")))
    mas.append(d)
a = np.array(mas)
a = a.transpose()
print(a)