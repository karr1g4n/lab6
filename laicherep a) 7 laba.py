str1=str(input("Введіть елементи: "))
str2=" "
digit=('0','1','2','3','4','5','6','7','8','9',",",":",".")

if str1[0]!=" ":
    for i in range(0,len(str1),1):
        if str1[i]==" ":
            break
    for c in str1[0:i]:
        if c not in digit:
            str2=str2+c
    print(str2)