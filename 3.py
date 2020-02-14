from enum import Enum

class converter (Enum):
        USD = 1
        EUR = 2
        CZK = 3
        PLN = 4

print("які є converter")

print( "USD = 1  " "EUR = 2 " "CZK = 3 " "PLN = 4 ")

while True:
    try:
        x= float(input('money:'))
        break
    except ValueError:
        print('money:')
while True:
    try:
        p = int(input('currency:'))
        break
    except ValueError:
        print('currency:')
if p==converter.USD.value:
    print(x, "* 24.52 =", x * 24.52)
if p == converter.EUR.value:
    print(x, "* 26.65 =", x * 26.65)
if p == converter.CZK.value:
    print(x, "* 1.07 =", x * 1.07)
if p == converter.PLN.value:
    print(x, "* 6.27 =", x * 6.27)

