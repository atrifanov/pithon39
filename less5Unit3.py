with open('file3.txt', encoding='utf-8') as fh:
    e_dict = {line.split()[0]: float(line.split()[1]) for line in fh}
    print(f"Средняя зарплата:  {round(sum(e_dict.values()) / len(e_dict), 3)}\n",
          f'Сотрудники с низкой зарплатой: {[el[0] for el in e_dict.items() if el[1] < 20]}')
