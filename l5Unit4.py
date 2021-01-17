file = 'file2.txt'
translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
translate = []

with open(file, encoding='utf-8') as fl:
    for line in fl:
        a = line.split(' — ')
        if a[0] in translater:
            word = translater[a[0]]
            translate.append(word + ' - ' + a[1])
with open('fileTr1.txt', 'w', encoding='utf-8') as fl1:
    fl1.writelines(translate)
