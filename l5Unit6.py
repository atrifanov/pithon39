subjects = {}
with open('fileS.txt', encoding='utf-8') as fl:
    lines = fl.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())

print(subjects)
