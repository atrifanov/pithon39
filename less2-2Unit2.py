a = input('Введите элементы списка через пробел, по завершении нажмите "Enter" - ')
a = a.split()
print(f'Ваш список выглядит следующим образом:  {a}')
b = []
i = 0
while i < len(a) - 1:
    b.insert(i, a[i + 1])
    b.insert(i + 1, a[i])
    i += 2
if len(a) % 2 != 0:
    b.append(a[len(a) - 1])

print(f'Ваш измененный список выглядит следующим образом:  {b}')
