import numpy as np
a = 3
b = 3
mas = []
mas_2=[]
for i in range(a):
    d=[]
    for j in range(b):
        d.append(int(input("введите первую матрицу по елементно:")))
    mas.append(d)
for i in range(a):
    c=[]
    for j in range(b):
        c.append(int(input("введите вторуюматрицу по елементно:")))
    mas_2.append(c)
c=np.array(mas)
b=np.array(mas_2)
print(c.dot(b))