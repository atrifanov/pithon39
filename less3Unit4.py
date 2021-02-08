def my_func (a, b):
    return 1 if b == 0 else my_func(a, b + 1) * 1 / a

print(my_func(3, -2))
