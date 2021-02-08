def my_func(a, b):
    try:
        a, b = int(a), int(b)
        c = a / b
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    return round(c, 4)

print(my_func(input('Введите первое число '), input('Введите второе число ')))
