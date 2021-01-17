file = 'new_file.txt'
while True:
        user_input = input('Введите произвольную строку: ')
        if not user_input:
            break

        try:
            with open(file, 'a', encoding='utf-8') as fh:
                fh.write(f'{user_input}\n')
        except IOError as e:
            print(e)
            break
