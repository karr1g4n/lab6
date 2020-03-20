import numpy as np
a = 4
b = 4
mas = []
digit=[1,2,3,4,5,6,7,8,9,]
for i in range(a):
    d = []
    for j in range(b):
        d.append(input("введите :"))
    mas.append(d)
for i in range(2):
    for j in range(2):
        if mas[i][j] not in digit:
            mas[i][j]="0"
g=np.array(mas)
print(g)