results = [{}, {}]
with open('file7.txt', encoding='utf-8') as fl:
    for line in fl.readlines():
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)
        results[1]['average_profit'] = round(sum(profit for _, profit in results[0].items() if profit > 0) / len(results[0]))
    print(results)
from json import dumps
with open('fileFirm.json', "w", encoding='utf-8') as fl:
    fl.write(dumps(results))
