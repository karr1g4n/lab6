while True:
    while True:
        try:
            t=int(input('Input time '))
        break
            except ValueError:
            print(' TIME!!')
a=t%6
if 1<=a<=3:
    print(' green')
elif a==4:
    print(' yellow')
else:
    print('red')
