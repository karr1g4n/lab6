from enum import Enum
class month (Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season (Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
while True:
    try:
        s=int(input('month:'))
        break
    except ValueError:
        print("month number")
if s==month.December.value or s==month.January.value or s==month.February.value:
    print(f'{season.Winter.name}')
elif s==month.March.value or s==month.April.value or s==month.May.value:
    print(f'{season.Spring.name}')
elif s==month.June.value or s==month.July.value or s==month.August.value:
    print(f'{season.Summer.name}')
else:
    print(f'{season.Autumn.name}')