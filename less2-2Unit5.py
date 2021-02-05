my_list = [8, 6, 4, 2, 2]
a = int(input('Введите любое целое число от "0" до "10", по завершении нажмите "Enter" - '))
i = 0

for el in my_list:
    if el >= a:
        i += 1

my_list.insert(i, a)
print(my_list)
