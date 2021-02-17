translater = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}

with open('fileTr1.txt', 'w', encoding='utf-8') as fl1:
    with open('file4.txt', encoding='utf-8') as fl:
        fl1.writelines([line.replace(line.split()[0], translater.get(line.split()[0])) for line in fl])
