# Задача про спортсмена
a = int(input("Введте результат пробежки в первый день - "))
b = int(input("Введте желаемый результат пробежки - "))
i = 1
if a >= b:
    print("Вы уже достигли желаемого результата")
else:
    while a < b:
        print(F'{i}-й день: {a}')
        a = a * 0.1 + a
        i = i + 1
print(F'{i}-й день: {a}')
print(F'На {i} день Вы достигнете желаемого результата не менее {b}, если будете добавлять 10% ежедневно')
