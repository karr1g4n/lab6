days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)

while True:
    while True:
        try:
            d = int(input("Введіть день:"))
            if d not in days:
                print('Не правильное количество дней')
                continue
            break
        except ValueError:
            print("тільки цифри")
    while True:
        try:
            m = int(input("Введіть місяць: "))
            if m not in months:
                print('Не правильное количество month')
                continue
            break
        except ValueError:
            print("тільки цифри!")
    while True:
        try:
            y = int(input("Введіть рік : "))
            if y not in years:
                print("рік повинен бути в діапазоні 1901 - 2019")
                continue
            break
        except ValueError:
         print("тільки цифри")

         days_in_february == 28

    if y % 4 == 0:
        days_in_february = 29
    months_list = [['Январь', 31], ['Февраль', days_in_february ], ['Март', 31], ['Апрель', 30], ['Май', 31],
                   ['Июнь', 30], ['Июль', 31],
                   ['Август', 31], ['Сентябрь', 30], ['Октябрь', 31], ['Ноябрь', 30], ['Декабрь', 31]]
    if d > months_list[m - 1][1]:
        print('Не правильное количество дней')
        continue
 
    day, month, year = d, m, y
    day -= 1
    month -= 1
    if day < 1:
        month -= 1
        day = months_list[month][1]
    if month < 0:
        year -= 1
    previous_day = f'previous day: {day}:{months_list[month][0]}:{year}'

    day, month, year = d, m, y
    day += 1
    month -= 1
    if day > months_list[month][1]:
        month += 1
        day = 1
    if month > 11:
        month = 0
        year += 1
    next_day = f'next day: {day}{months_list[month][0]}{year}'

    print(previous_day)
    print(next_day)

