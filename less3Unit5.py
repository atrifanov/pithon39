def my_funk():
    rez2 = []
    while True:
        stroka = input('Введите строку чисел через пробел. Если захотите выйти из программы, введите Q - ').split()
        print('Вы ввели: ')
        print(stroka)
        i = 0
        while i <= len(stroka) - 1:
            if stroka[i].upper() == 'Q':
                print('Сумма введеных чисел равна: ')
                print(sum(rez2))
                return
            else:
                rez1 = int(stroka[i])
                rez2.append(rez1)
                i += 1
        print('Сумма введеных чисел равна: ')
        print(sum(rez2))
my_funk()
