from collections import OrderedDict

num = int(input('Введите количество предприятий: '))
institutions = [OrderedDict() for x in range(num)]
average = 0
for item in institutions:
    item['name'] = input('Название организации: ')
    item['1'] = int(input('Доход за 1 квартал:: '))
    item['2'] = int(input('Доход за 2 квартал:: '))
    item['3'] = int(input('Доход за 3 квартал:: '))
    item['4'] = int(input('Доход за 4 квартал:: '))
    item['aver'] = float((item['1'] + item['2'] + item['3'] + item['4']) / 4)
    average += item['aver']
    print('*' * 50)
average = average / num

print('Список предприятий, чья прибыль выше среднего:')
for item in institutions:
    if item['aver'] > average:
        print(item['name'])
print('*' * 50)
print('Список предприятий, чья прибыль ниже среднего:')
for item in institutions:
    if item['aver'] < average:
        print(item['name'])