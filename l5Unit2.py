file = 'new_file.txt'
try:
    with open(file, encoding='utf-8') as fh:
        lines = [line for line in fh.readlines() if line != '\n']
        print(f"В файле непустых строк:", len(lines))
except IOError as e:
    print(e)
for line in lines:
    print(f'Строка {line[:9]}... содержит {len(line.split())} слов')
