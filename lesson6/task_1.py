# Выбрала задачу №1 из урока №3:
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# Данная задача разбита на 3 блока,
# каждый блок - это один из вариантов решения задачи,
# количество памяти считается отдельно на каждый блок,
# память на кранение переменных с используемыми показателями
# памяти не учитывается при первом выводе. Но для полноты картитины я укажу полное
# количество памяти ниже.
# Вывод результатов самой программы не осуществляю, так как здесь он
# не несёт смысловой нагрузки


import sys

print(sys.version, sys.platform)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32

# Вариант 1

print('Первый вариант решения задачи')
print("*" * 50)

count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0

start_size = sys.getsizeof(count_2) * 8
start_id = id(count_2)

for i in range(2, 100):
    if i % 2 == 0:
        count_2 += 1
    if i % 3 == 0:
        count_3 += 1
    if i % 4 == 0:
        count_4 += 1
    if i % 5 == 0:
        count_5 += 1
    if i % 6 == 0:
        count_6 += 1
    if i % 7 == 0:
        count_7 += 1
    if i % 8 == 0:
        count_8 += 1
    if i % 9 == 0:
        count_9 += 1

if sys.getsizeof(2) == sys.getsizeof(100):
    counter_size = sys.getsizeof(2) * (len(range(2, 100)))
else:
    counter_size = 0

if sys.getsizeof(count_2) == sys.getsizeof(count_9):
    finish_size = sys.getsizeof(count_2) * 8

if start_id == id(count_2):
    print(f'Суммарное количество используетмой памяти для данного варианта: {counter_size + finish_size}')
else:
    print(f'Суммарное количество используетмой памяти для данного варианта: {start_size + counter_size + finish_size}')
# Суммарное количество используетмой памяти для данного варианта: 1580

print('Всего памяти для блока:',
      start_size + counter_size + finish_size + sys.getsizeof(start_size) + sys.getsizeof(start_id) + sys.getsizeof(
          counter_size) + sys.getsizeof(finish_size))
# Всего памяти для блока: 1640

# Вариант 2
print()
print('Второй вариант решения задачи')
print("*" * 50)

count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0

start_size = sys.getsizeof(count_2) * 8
start_id = id(count_2)

array = [item for item in range(2, 100)]

array_size = sys.getsizeof(array)

for i in array:
    if i % 2 == 0:
        count_2 += 1
    if i % 3 == 0:
        count_3 += 1
    if i % 4 == 0:
        count_4 += 1
    if i % 5 == 0:
        count_5 += 1
    if i % 6 == 0:
        count_6 += 1
    if i % 7 == 0:
        count_7 += 1
    if i % 8 == 0:
        count_8 += 1
    if i % 9 == 0:
        count_9 += 1

# Так как значения i менялись, менялись и ссылки на значение переменной
i_size = sys.getsizeof(i) * len(array)

if sys.getsizeof(count_2) == sys.getsizeof(count_9):
    finish_size = 0
else:
    finish_size = sys.getsizeof(count_2) * 8

if start_id == id(count_2):
    print(f'Суммарное количество используетмой памяти для данного варианта: {array_size + i_size + finish_size}')
else:
    print(
        f'Суммарное количество используетмой памяти для данного варианта: {start_size + array_size + i_size + finish_size}')
# Суммарное количество используетмой памяти для данного варианта: 1928

print('Всего памяти для блока:',
      start_size + array_size + i_size + finish_size + sys.getsizeof(start_size) + sys.getsizeof(
          start_id) + sys.getsizeof(array_size) + sys.getsizeof(i_size) + sys.getsizeof(finish_size))
# Всего памяти для блока: 2000


# Варинат 3
print()
print('Третий вариант решения задачи')
print("*" * 50)

array = list([item for item in range(2, 100)])
array_size = sys.getsizeof(array)

count = [0] * 8
start_count_size = sys.getsizeof(count)
for i in array:
    if i % 2 == 0:
        count[0] += 1
    if i % 3 == 0:
        count[1] += 1
    if i % 4 == 0:
        count[2] += 1
    if i % 5 == 0:
        count[3] += 1
    if i % 6 == 0:
        count[4] += 1
    if i % 7 == 0:
        count[5] += 1
    if i % 8 == 0:
        count[6] += 1
    if i % 9 == 0:
        count[7] += 1
i_size = sys.getsizeof(i) * len(array)

if sys.getsizeof(count) == start_count_size:
    finish_count_size = 0
else:
    finish_count_size = sys.getsizeof(count)

print(
    f'Суммарное количество используетмой памяти для данного варианта: {start_count_size + array_size + i_size + finish_count_size}')
# Суммарное количество используетмой памяти для данного варианта: 1940

print('Всего памяти для блока:',
      start_count_size + array_size + i_size + finish_count_size + sys.getsizeof(start_count_size) + sys.getsizeof(
          array_size) + sys.getsizeof(i_size) + sys.getsizeof(finish_count_size))
# Всего памяти для блока: 1994


# Вывод:
# Из трёх вариантов решения задачи меньше всего занимает памяти первый вариант,
# что обусловлено отсутствием в данном решении итерируемых
# конструкций, таких как списки. Наибольшее количество памяти уходит
# на обход цикла для определения количества кратных чисел, согласно условию.
# Наиболее затратным по количеству занимаемой памяти выходит третий вариант
# решения задачи. Варианты №3 и №2 более ресурсоёмки из-за использования
# итерационных конструкций. Стоит отметить, что разница в затратах памяти
# обусловлена использованием массива вместо списка переменных в третием варианте
# решения. При этом, разница в ресурсах решения №2 и №3 достаточно мала.