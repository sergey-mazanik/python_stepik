# def keanu_reeves():
#     print("YOU'RE BREATHTAKING")

# def say_hello_world(name):
#     print(f'{name} говорит hello world!')
#
# # say_hello_world(input())

# def summa_n(t):
#     S = 0
#     for i in range(1, t+1):
#         S = S + i
#     print(f'Я знаю, что сумма чисел от 1 до {t} равна {S}')
#
# # summa_n(t := int(input()))

# def exponentiation(x):
#     print(f'{x ** 2} {x ** 3}')
#
# # exponentiation(10)

# def sum_num(name):
#     lst = []
#     for i in name:
#         if i.isdigit():
#             lst.append(int(i))
#     print(sum(lst))
#
# sum_num(input())

# def get_body_mass_index(x, y):
#     z = x / ((y / 100) ** 2)
#     if z < 18.5:
#         print('Недостаточная масса тела')
#     elif 18.5 <= z <= 25:
#         print('Норма')
#     else:
#         print('Избыточная масса тела')
#
#
# get_body_mass_index(170, 200)

# def check_password(password):
#     count_digit = 0
#     count_upper = 0
#     count_spec = 0
#     for i in password:
#         if i.isdigit():
#             count_digit += 1
#         if i.isupper():
#             count_upper += 1
#         if i in '!@#$%*':
#             count_spec += 1
#     if count_digit >= 3 and count_upper > 0 and count_spec > 0 and len(password) >= 10:
#         print('Perfect password')
#     else:
#         print('Easy peasy')
#
#
# check_password('Qwerty1357!')
# check_password('Qwerty1357)')
# check_password('Qwerty17!')
# check_password('qwerty')

# def count_letters(letters):
#     count_upper = 0
#     count_lower = 0
#     for i in letters:
#         if i.isupper():
#             count_upper += 1
#         if i.islower():
#             count_lower += 1
#     print(f'Количество заглавных символов: {count_upper}\nКоличество строчных символов: {count_lower}')
#
#
# count_letters('Привет, Старина')
# count_letters('QWERTY')

# def repeat_please_n_times(n):
#     for i in range(n):
#         print('Just do it')
#
#
# repeat_please_n_times(5)

# объявление функции
# def is_between(name, surname, middlename):
#     if surname <= name <= middlename or surname >= name >= middlename:
#         print('True')
#     else:
#         print('False')
#
# # считываем данные
# a, b, c = map(int, input().split())
#
# # вызываем функцию
# is_between(a, b, c)

# объявление функции
# def count_letter(text, letter):
#     print(text.count(letter))
#
#
# # считываем данные
# text = input()
# symbol = input()
# # вызываем функцию
# count_letter(text, symbol)

# объявление функции
# def print_initials(name, surname, middlename):
#     print(f'{surname.capitalize()} {name[0].upper()}.{middlename[0].upper()}.')
#
# # считываем данные
# name = input()
# surname = input()
# middlename = input()
#
# # вызываем функцию
# print_initials(name, surname, middlename)

# assert 200 > 100
# assert [100] * 4 < [100, 100, 100, 10000]
# assert sum([1, 3, 5]) == sum([6, 3])
# assert max(3, -1, 9) != -1
# print('Проверки пройдены')

# def is_person_teenager(x):
#     if 12 <= x <= 17:
#         return True
#     return False
#
#
# print(is_person_teenager(int(input())))

# def factorial(n):
#     pr = 1
#     for i in range(2, n + 1):
#         pr *= i
#     return pr
#
#
# n = int(input())
# print(factorial(n))

# def generate_fizz_buzz_list(n):
#     mas = []
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             mas.append('FizzBuzz')
#         elif i % 3 == 0:
#             mas.append(('Fizz'))
#         elif i % 5 == 0:
#             mas.append('Buzz')
#         else:
#             mas.append(i)
#     return mas
#
#
# print(generate_fizz_buzz_list(3))
# print(generate_fizz_buzz_list(7))
# print(generate_fizz_buzz_list(15))
# print(generate_fizz_buzz_list(30))

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a%b
#     return a
#
# from functools import reduce
# x = int(input())
# lst = []
# for i in range(x):
#     lst.append(int(input()))
# print(reduce(gcd, lst))
#

# def find_duplicate(lst):
#     lst1 = []
#     for i in lst:
#         if lst.count(i) > 1 and i not in lst1:
#             lst1.append(i)
#     return lst1
#
#
# assert find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
# assert find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [2, 1]
# assert find_duplicate([1, 2, 3, 4]) == []
# assert find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]) == [8, 7, 6, 5, 4]
# print('Все успешно')

# def first_unique_char(s):
#     for i in s:
#         if s.count(i) == 1:
#             return s.index(i)
#     return '-1'
#
#
# s = input()
# print(first_unique_char(s))

# def format_name_list(names):
#     lst = []
#     for i in range(len(names)):
#         lst.append(names[i]['name'])
#     if len(lst) == 0:
#         return ''
#     if len(lst) == 1:
#         return lst[0]
#     if len(lst) == 2:
#         return lst[0] + ' и ' + lst[1]
#     s = ', '.join(lst[:-2])
#     s = s + ', ' + lst[-2] + ' и ' + lst[-1]
#     return s
#
#
# # код ниже не стоит удалять, он нужен для проверки
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
# assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
# assert format_name_list([{'name': 'Bart'}]) == 'Bart'
# assert format_name_list([]) == ''
# assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
# assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
# assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
# print('Проверки пройдены')

# def get_domain_name(url):
#     if 'www' in url:
#         url = url.split('.')
#         return url[1]
#     if 'http://' in url or 'https://' in url:
#         url = url.split('://')
#         url[1] = url[1].split('.')
#         return url[1][0]
#
#
# # код ниже не стоит удалять, он нужен для проверки
# # print(get_domain_name("www.xakep.ru"))
# assert get_domain_name("http://google.com") == "google"
# assert get_domain_name("http://google.co.jp") == "google"
# assert get_domain_name("www.xakep.ru") == "xakep"
# assert get_domain_name("https://youtube.com") == "youtube"
#
# assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
# assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
# assert get_domain_name("https://www.siemens.com") == 'siemens'
# assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
# assert get_domain_name("https://www.mywww.com") == 'mywww'
# print('Проверки пройдены')

# def factorial(n):
#     fact = 1
#     for num in range(2, n + 1):
#         fact *= num
#     return fact
#
# def trailing_zeros(n):
#     count = 0
#     a = factorial(n)
#     for i in str(a):
#         if i == '0':
#             count += 1
#         else:
#             count = 0
#     return count
#
#
# # код ниже не стоит удалять, он нужен для проверки
# assert trailing_zeros(0) == 0
# assert trailing_zeros(6) == 1
# assert trailing_zeros(30) == 7
# assert trailing_zeros(12) == 2
# print('Проверки пройдены')

# def count_AGTC(dna):
#     a = g = t = c = 0
#     for i in dna:
#         if i == 'A':
#             a += 1
#         elif i == 'G':
#             g += 1
#         elif i == 'T':
#             t += 1
#         else:
#             c += 1
#     my_tuple = tuple([a, g, t, c])
#     return my_tuple
#
#
# # код ниже не стоит удалять, он нужен для проверки
# assert count_AGTC('AGGTC') == (1, 2, 1, 1)
# assert count_AGTC('AAAATTT') == (4, 0, 3, 0)
# assert count_AGTC('AGTTTTT') == (1, 1, 5, 0)
# assert count_AGTC('CCT') == (0, 0, 1, 2)
# print('Проверки пройдены')
