from itertools import cycle, count

for i in count(int(input('Введите число. Затем для продолжения ввода новых чисел - "Enter", для выхода - "q" '))):
    print(i, end=' ')
    a = input()
    if a == 'q':
        break

b = input('Введите элементы через пробел. Затем для продолжения работы программы - "Enter", для выхода - "q" ').split()
с = cycle(b)
quit = None

while quit != 'q':
    print(next(с), end=' ')
    quit = input()
