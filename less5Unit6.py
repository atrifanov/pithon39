subjects = {}
with open('file6.txt', encoding='utf-8') as fl:
    for line in fl.readlines():
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(subjects)
