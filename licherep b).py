bookLibraryKeys = [input(f'Книга {i+1} : ') for i in range(int(input('Скільки книг : ')))]
bookLibrary = {i:[input(f'Автор "{i}" '), input(f'Рік "{i}" '), int(input(f'Кількість сторінок "{i}" ')), input(f'Тираж "{i}" ')] for i in bookLibraryKeys}

for i in bookLibrary.keys():
    if bookLibrary[i][2] >= 150:
        print(f'У книги під назвою "{i}" більше 150 сторінок')