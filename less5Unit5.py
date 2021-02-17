from random import randint
summ = 0
with open('fileNum.txt', 'w+', encoding='utf-8') as fl:
    fl.write(' '.join([str(randint(1, 100)) for _ in range(10)]))
    fl.seek(0)
    for i in fl.readline().split():
        summ += int(i)
print(summ)