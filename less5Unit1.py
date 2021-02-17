with open('file1.txt', 'w', encoding='utf-8') as fh:
    while True:
        user_input = input('Введите произвольную строку: ')
        fh.write(f'{user_input}\n')
        if not user_input:
            break
