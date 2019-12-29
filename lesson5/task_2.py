from collections import defaultdict, deque

def transform_to_dec(list_1, list_2):
    hex_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_1 = []
    dec_2 = []
    deque.reverse(list_1)
    for i in range(len(list_1)):
        if list_1[i] in 'abcdef':
            list_1[i] = list_1[i].upper()
        dec_1.append(hex_dec[list_1[i]])

    deque.reverse(list_2)
    for i in range(len(list_2)):
        if list_2[i] in 'abcdef':
            list_2[i] = list_2[i].upper()
        dec_2.append(hex_dec[list_2[i]])

    return dec_1, dec_2

def transform_to_hex(result):
    dec_hex = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
               9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    deque.reverse(result)
    for i in range(len(result)):
        result[i] = dec_hex[result[i]]
    return result

def hex_sum(list_1, list_2):
    hex_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    dec_1, dec_2 = transform_to_dec(list_1, list_2)

    if len(list_1) > len(list_2):
        for i in range(len(list_1) - len(list_2)):
            dec_2.append(0)
    if len(list_2) > len(list_1):
        for i in range(len(list_2) - len(list_1)):
            dec_1.append(0)

    flag = 0
    result = deque()
    for i in range(len(dec_1)):
        result.append(dec_1[i] + dec_2[i] + flag)
        if result[i] >= 16:
            flag = 1
            result[i] = hex_dec[str(result[i] - 16)]
        else:
            flag = 0


    return transform_to_hex(result)


def hex_mult(list_1, list_2):
    hex_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_1, dec_2 = transform_to_dec(list_1, list_2)
    list.reverse(dec_1)
    list.reverse(dec_2)
    flag = 0
    result = deque()
    buf = []
    for i in range(len(list_2)):
        for j in range(len(list_1)):
            buf.append(dec_1[j] * dec_2[i])
    # print(buf)
    arr = []
    # print(buf[3:len(list_1)])
    for i in range(0, len(buf), len(list_1)):
        # print(i)
        arr.append(list(buf[i:len(list_1)]))
        # print(buf[i:len(list_1)])
    # print(arr)
    # while True:
    #     for i in range(len(dec_1)):
    #         result.append(buf[i] * dec_2[i] + flag)
    # print(result[i])
    # if result[i] >= 16:
    #     flag = result[i] // 16
    #     result[i] = result[i] % 16
    # else:
    #     flag = 0
    return transform_to_hex(result)

worked_list = '012345689abcdefABCDEF'
num_1, num_2 = input('Введите два шестрнадцатеричных числа через пробел:\n').split(' ')

list_1 = deque(num_1)
list_2 = deque(num_2)

for i in list_1:
    if i not in worked_list:
        print("Вы неправильно ввели первое число. Перезапустите программу!")
        break
for i in list_2:
    if i not in worked_list:
        print("Вы неправильно ввели второе число. Перезапустите программу!")
        break

res = defaultdict()
res['sum'] = hex_sum(list_1, list_2)
res['mult'] = hex_mult(list_1, list_2)

print(f'Результат сложения 2х чисел: {res["sum"]}')
print(f'Результат умножения 2х чисел: {res["sum"]}')