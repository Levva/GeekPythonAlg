import hashlib

def Rabin_Karp(s: str) -> int:
    assert len(s) > 0, 'Строки не могут быть пустыми'

    count = 0
    count_zerro = 0
    len_sub = 0

    for h in range(len(s)):
        for i in range(h, len(s)+1):
            subs = s[h:i]
            # Раскомментировать, чтобы увидеть подстроки
            # print(subs)
            h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
            len_sub = len(subs)
            for j in range(len(s) - len_sub + 1):
                if h_subs == hashlib.sha1(s[j:j + len_sub].encode('utf-8')).hexdigest():
                    if s[j:j+len_sub] == subs:
                        count += 1
                    if len(subs) == len(s):
                        count_zerro += 1
                    if len(subs) == 0:
                        count_zerro += 1

    return count - count_zerro


a = input('Введите строку: ')
if len(a) == 0:
    a = '01234567890123456789'
    print(f'Была введена пустая строка, для дальнейшей работы используется строка поумолчанию: "{a}"')

count_substr = Rabin_Karp(a)

print(f'Подстрока найдено подстрок: {count_substr}' if count_substr > 0 else 'Посдстрок не найдено')
