file = 'new_file.txt'
summa = 0
count = 0
persons = []
try:
    with open(file, encoding='utf-8') as fh:
        for line in fh:
            print(line)
            tokens = line.split()
            if int(tokens[1]) <= 20:
                persons.append(tokens[0])
            summa += int(tokens[1])
            count += 1
        result = summa / count
    print(f"persons with small salary: {persons}")
    print(f"average result: {result}")
except IOError as e:
    print(e)
