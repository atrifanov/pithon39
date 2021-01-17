summ = 0
with open('fileNum.txt', 'w', encoding='utf-8') as fl:
    print('1 2 3 4 5 6 7 8 9', file=fl)

with open('fileNum.txt', 'r', encoding='utf-8') as fl:
    data = fl.readline()
    print(data)
    for i in data.split():
        summ += int(i)
print(summ)
