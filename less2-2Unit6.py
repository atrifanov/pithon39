result = []
analitics = {'название': [], 'цена': [], 'количество': [], 'ед. изм.': []}
store = {'название': '', 'цена': '', 'количество': '', 'ед. изм.': ''}
i = 1

while True:
    for p in store.keys():
        b = input(f'Введите {p}: ')
        store[p] = b
        analitics[p].append(store[p])
    result.append((i, tuple(store.items())))
    print(f'\nСтруктура товаров\n{result}')
    print('\nТекущая аналитика:')
    for key, value in analitics.items():
       print(f'\n{key}: {value}')
    i += 1
    if input('Хотите продолжить вводить данные? Тогда жмите "Enter". Для выхода жмите "Q" :').upper() == 'Q':
        break