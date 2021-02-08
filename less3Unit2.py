params = {
    'name': input('Введите имя - '),
    'last name': input('Введите фамилию - '),
    'phone': input('Введите телефон - '),
    'birthday': input('Введите год рождения - '),
    'email': input('Введите электронный адрес - '),
    'city': input('Введите город проживания - '),
}
def my_func(**params):
    return params

print(my_func(**params))
