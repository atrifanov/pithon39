
# Задача по вводу данных
name = input("Введте Ваше имя - ")
fmale = input("Введите Вашу фамилию - ")
age = int(input("Введите Ваш возраст - "))
child = int(input("Введите количество Ваших детей - "))
print(F'Ваше имя - {name}\nВаша фамилия - {fmale}\nВаш возраст - {age}\nУ Вас  {child} ребенка')

# Задача по переводу секунд в иной формат
time = int(input("Введите время в секундах - "))
hour = time // 3600
minute = time % 3600 // 60
second = time % 3600 % 60
print(F'Введеное время в формате чч:мм:сс - {hour:02}:{minute:02}:{second:02}')

# Задача по работе с числом "n"
n = input("Введте любое целое число 'n' - ")
nn = n + n
nnn = nn + n
n = int(n)
nn = int(nn)
nnn = int(nnn)
print(F'Сумма чисел n + nn + nnn будет равна - {n + nn + nnn}')