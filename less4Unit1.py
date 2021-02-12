from sys import argv

def my_func():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Зарплата равна - {time * rate + bonus}')
    except ValueError:
        print('Ошибка ввода параметров')

my_func()
