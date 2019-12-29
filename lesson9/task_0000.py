import hashlib

def is_eq_str(a: str, b: str, verbouse = False):
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbouse:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha == hb

a = input('Введите строку 1: ')
b = input('Введите строку 2: ')

print('Строки одинаковые' if is_eq_str(a, b, True) else 'Сроки разные')