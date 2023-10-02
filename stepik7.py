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

# def add_binary(a, b):
#     'Возвращает сумму чисел a и b в двоичном виде'
#     binary_sum = bin(a+b)[2:]
#     return binary_sum
#
#
# print(add_binary.__doc__)

# from typing import List, Optional
#
#
# def first_repeated_word(s: str) -> str:
#     'Находит первый дубль в строке'
#     s = s.split()
#     lst: List[Optional[str]] = []
#     for i in s:
#         if i not in lst:
#             lst.append(i)
#         else:
#             return i
#
#
# assert first_repeated_word('hello hi hello') == 'hello'
# assert first_repeated_word('hello hi Hello') is None
# assert first_repeated_word('ab ca bc ab') == 'ab'
# assert first_repeated_word('ab ca bc Ab cA aB bc') == 'bc'
# print('Проверки пройдены')

# def shift_letter(letter: str, shift: int) -> str:
#     'Функция сдвигает символ letter на shift позиций'
#     new_letter: str | None = chr(((ord(letter) - ord('a') + shift) % 26) + 97)
#     return new_letter
#
#
# assert shift_letter('z', 5)
# assert shift_letter('w', 28)
# assert shift_letter('w', -26)
# assert shift_letter('w', -27)
# assert shift_letter('a', 53)

# def shift_letter(letter: str, shift: int) -> str:
#     'Функция сдвигает символ letter на shift позиций'
#     new_letter: str | None = chr(((ord(letter) - ord('a') + shift) % 26) + 97)
#     return new_letter
# def caesar_cipher(s: str, shift: int) -> str | None:
#     'Шифр цезаря'
#     rez: str | None= ''
#     for i in s:
#         if i.isalpha():
#             rez += shift_letter(i, shift)
#         else:
#             rez += ' '
#     return rez
#
#
# # print(caesar_cipher('leave out all the rest', -1))
# assert caesar_cipher('leave out all the rest', -1) == 'kdzud nts zkk sgd qdrs'
# assert caesar_cipher('one more light', 3) == 'rqh pruh oljkw'
# assert caesar_cipher('lost in the echo', 27) == 'mptu jo uif fdip'
# assert caesar_cipher('from the inside', 10) == 'pbyw dro sxcsno'
# assert caesar_cipher('leave out all the rest', -4) == 'hawra kqp whh pda naop'
# assert caesar_cipher('one more light', -33) == 'hgx fhkx ebzam'
# print('Проверки пройдены')

# MIN_DRIVING_AGE = 18
#
# def allowed_driving(name: str, age: int) -> None:
#     if age >= MIN_DRIVING_AGE:
#         print(f'{name} может водить')
#     else:
#         print(f'{name} еще рано садиться за руль')

# def get_word_indices(strings: list[str]) -> dict:
#     d = {}
#     for i in range(len(strings)):
#         for j in strings[i].lower().split():
#             if j not in d:
#                 d[j] = [i]
#             else:
#                 d[j].append(i)
#     return d
#
#
# assert get_word_indices(['a', 'v', 'v', 'e', 'v', 'V']) == {'a': [0], 'v': [1, 2, 4, 5], 'e': [3]}
# assert get_word_indices(['This is a string',
#                          'test String',
#                          'test',
#                          'string']) == {'this': [0], 'is': [0], 'a': [0],
#                                         'string': [0, 1, 3], 'test': [1, 2]}
#
# assert get_word_indices(['Look at my horse',
#                          'my horse',
#                          'is amazing']) == {'look': [0], 'at': [0], 'my': [0, 1],
#                                             'horse': [0, 1], 'is': [2], 'amazing': [2]}
#
# assert get_word_indices([]) == {}
#
# assert get_word_indices(['Avada Kedavra',
#                          'avada kedavra',
#                          'AVADA KEDAVRA']) == {'avada': [0, 1, 2],
#                                                'kedavra': [0, 1, 2]}

# объявление функции
# def replace(text: str, old: str, new: str = ''):
#     for i in text:
#         if i == old:
#             text = text.replace(i, new)
#     return text
#
#
# assert replace('Нет', 'т') == 'Не'
# assert replace('Bella Ciao', 'a') == 'Bell Cio'
# assert replace('nobody; i myself farewell analysis', 'l', 'z') == 'nobody; i mysezf farewezz anazysis'
# assert replace('commend me to my kind lord meaning', 'M', 'w') == 'commend me to my kind lord meaning'

# def make_header(s: str, n: int = 1) -> str:
#     return f'<h{n}>{s}</h{n}>'
#
# print('Tests begin...')
# assert make_header('Нет') == '<h1>Нет</h1>'
# assert make_header('Bella Ciao', 4) == '<h4>Bella Ciao</h4>'
# assert make_header('Go little rock star', 6) == '<h6>Go little rock star</h6>'
# assert make_header('Девальвации не будет. Твердо и четко') == '<h1>Девальвации не будет. Твердо и четко</h1>'
# print('Tests completed successfully')

# def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
#     matrix = []
#     for i in range(size):
#         matrix.append([0] * size)
#     for i in range(size):
#         for j in range(size):
#             if i == j:
#                 matrix[i][j] = j + 1
#             elif i < j:
#                 matrix[i][j] = up_fill
#             elif i > j:
#                 matrix[i][j] = down_fill
#     return matrix
#
#
# assert create_matrix() == [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
# assert create_matrix(4) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
#
# assert create_matrix(up_fill=7) == [[1, 7, 7],
#                              [0, 2, 7],
#                              [0, 0, 3]]
#
# assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
#                                           [9, 2, 7],
#                                           [9, 9, 3]]
#
#
# assert create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
#                                                   [9, 2, 7, 7],
#                                                   [9, 9, 3, 7],
#                                                   [9, 9, 9, 4]]
# print('Tests completed successfully')

# def count_args(*args):
#     s = 0
#     for i in args:
#         s += 1
#     return s
#
#
# assert count_args(1, 2, 3) == 3
# assert count_args(1, 3) == 2
# assert count_args(2) == 1
# assert count_args() == 0
# print('Tests completed successfully')

# def check_sum(*args: int):
#     if sum(args) >= 50:
#         text = "verification passed"
#     else:
#         text = "not enough"
#
#     print(text)

# def multiply(*args: int):
#     s = 1
#     for i in args:
#         s *= i
#     return s
#
# print(multiply(2))

# def only_one_positive(*args: int) -> bool:
#     count = 0
#     if len(args) == 0:
#         return False
#     else:
#         for i in args:
#             if i > 0:
#                 count += 1
#         return count == 1
#
#
# print(only_one_positive())
# assert only_one_positive(0,0,0,0,5430,0,0,0,0,0) == True
# assert only_one_positive() == False

# def print_goods(*args):
#     c = 1
#     for i in args:
#         if type(i) == str and len(i) > 0:
#             print(f'{c}. {i}')
#             c += 1
#     if c == 1:
#         print('Нет товаров')
#
#
# assert print_goods(1, True, 'Грушечка', '', 'Pineapple')

# def info_kwargs(**kwargs):
#     for i in sorted(kwargs):
#         print(f"{i} = {kwargs[i]}")
#
# print(info_kwargs(first_name="John", last_name="Doe", age=33))

# def create_actor(**kwargs):
#     f = {
#         'name': 'Райан',
#         'surname': 'Рейнольдс',
#         'age': 46,
#     }
#     return f | kwargs
#
#
# assert create_actor() == {
#     'name': 'Райан',
#     'surname': 'Рейнольдс',
#     'age': 46, }
# assert create_actor(height=190, movies=['Дедпул', 'Главный герой']) == {
#     'name': 'Райан',
#     'surname': 'Рейнольдс',
#     'age': 46,
#     'height': 190,
#     'movies': ['Дедпул', 'Главный герой']}
# assert create_actor(name='Jack', age=20) == {
#     'name': 'Jack',
#     'surname': 'Рейнольдс',
#     'age': 20, }
# print('Tests completed successfully')


# def print_from(n: int) -> None:
#     if n > 0:
#         print(n)
#         print_from(n - 1)
#
#
# print_from(5)


# def print_to(n: int) -> None:
#     if n > 0:
#         print_to(n - 1)
#         print(n)
#
# print_to(5)

# n = int(input())
# lst = input().split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
#
#
# def zero(n):
#     if n != 0:
#         print(lst[n - 1], end=' ')
#         zero(n - 1)
#
#
# zero(len(lst))


# def double_fact(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return n * double_fact(n - 2)
#
#
# print(double_fact(10))


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(n := int(input())))


# def tribonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
#
#
# print(tribonacci(8))


# def get_combin(n, k):
#     if k == 0:
#         return 1
#     if k == n:
#         return 1
#     return get_combin(n - 1, k) + get_combin(n - 1, k - 1)
#
#
# print(get_combin(5, 2))


# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     if m > 0 and n == 0:
#         return ackermann(m - 1, 1)
#     if m > 0 and n > 0:
#         return ackermann(m - 1, ackermann(m, n - 1))
#
#
# print(ackermann(3,2))


# def list_sum_recursive(lst: list):
#     if len(lst) == 0:
#         return 0
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + list_sum_recursive(lst[1:])
#
#
# print(list_sum_recursive([1, 2, 3, 4, 5]))


# def flatten(s: list):
#     if not s:
#         return []
#     if isinstance(s[0],list):
#         return flatten(s[0]) + flatten(s[1:])
#     return s[:1] + flatten(s[1:])
#
#
# assert flatten([1, [2, 3, [4]], 5]) == [1, 2, 3, 4, 5]
# assert flatten([1, [2, 3], [[2], 5], 6]) == [1, 2, 3, 2, 5, 6]
# assert flatten([[[[9]]], [1, 2], [[8]]]) == [9, 1, 2, 8]
# print('Tests completed successfully')


# def flatten_dict(d: dict, s: str = ''):
#     res = {}
#     for k, v in d.items():
#         if isinstance(v, int):
#             res.update({s + k: v})
#         if isinstance(v, dict):
#             res.update(flatten_dict(v, s + k + '_'))
#     return res
#
#
# assert flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}) == {'Q_w_E_r_T_y': 123}
# assert flatten_dict({'Germany_berlin': 7,
#                      'Europe_italy_Rome': 3,
#                      'USA_washington': 1,
#                      'USA_New York': 4}) == {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1,
#                                              'USA_New York': 4}
# assert flatten_dict({'a': 100, 'b': 200}) == {'a': 100, 'b': 200}
# assert flatten_dict(
#     {'Geeks': {'for': {'for': 1, 'geeks': 4}}, 'for': {'geeks': {'Geeks': 3}}, 'geeks': {'Geeks': {'for': 7}}}) == {
#            'Geeks_for_geeks': 4, 'for_geeks_Geeks': 3, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1}
# assert flatten_dict({"a": 1,
#                      "b": {
#                          "c": 2,
#                          "d": 3,
#                          "e": {
#                              "f": 4,
#                              '6': 100,
#                              '5': {"g": 6},
#                              "l": 1,
#                          }
#                      }}) == {'a': 1, 'b_c': 2, 'b_d': 3, 'b_e_f': 4, 'b_e_6': 100, 'b_e_5_g': 6, 'b_e_l': 1}
# print('Tests completed successfully')


# # функция merge_two_list должна объединить два списка
# def merge_two_list(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += a[i:]
#     if j < len(b):
#         c += b[j:]
#     return c
#
#
# # функция merge_sort должна выполнить сортировку
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     middle = len(s) // 2
#     left = merge_sort(s[:middle])
#     right = merge_sort(s[middle:])
#     return merge_two_list(left, right)
#
#
# print(merge_sort([6, 2, 19, 5, 10, 7, 11]))


# def quick_sort(s):
#     if len(s) <= 1:
#         return s
#     elem = s[0]
#     left = list(filter(lambda x: x < elem, s))
#     center = [i for i in s if i == elem]
#     right = list(filter(lambda x: x > elem, s))
#
#     return quick_sort(left) + center + quick_sort(right)
#
#
# print(quick_sort([16, 19, 2, 12, 20, 15, 20, 15]))



# adding_10 = lambda x: x + 10
# print(adding_10(10))


# starts_with = lambda s: True if s[0] == 'W' else False
# print(starts_with('world'))


# sale_lambda = lambda x: x * 0.9
# print(sale_lambda(10))


# sale_lambda = lambda x: x * 0.9 if x > 50 else x
# print(sale_lambda(12.33))


# sq = lambda x, y: x ** 2 + y ** 2
# print(sq(5, 3))


# average = lambda *args: sum(args) / len(args)
# print(average(5, 3, 2, 2))


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
# subject_marks = sorted(subject_marks, key=lambda x: x[1])
# [print(*tu, sep=' ') for tu in subject_marks]


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
#                  ('Physics', 93), ('History', 82), ('French', 78),
#                  ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# subject_marks = sorted(subject_marks, key=lambda x: -x[1])
# [print(*tu, sep=' ') for tu in subject_marks]


# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# subject_marks = sorted(subject_marks, key=lambda x: (-x[1], x[0]))
# [print(*tu, sep=' ') for tu in subject_marks]


# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
#
# for i in sorted(models, key=lambda x: x['color']):
#     print(f'Производитель: {i["make"]}, модель: {i["model"]}, цвет: {i["color"]}')

# lst = [i.split(':') for i in iter(input, 'конец')]
# for i in sorted(lst, key=lambda x: int(x[1]), reverse=True):
#     print(i[0])


# a = {}
# n = int(input())
# for i in range(n):
#     string = input()
#     if string not in a:
#         a[string] = 1
#     else:
#         a[string] += 1
#
# minimum = min(a.items(), key=lambda x: x[1])
# maximum = max(a.items(), key=lambda x: x[1])
# if len(a) >= 1:
#     print(*maximum, sep=', ')
#     print(*minimum, sep=', ')


# n = int(input())
# k = {}
# for i in range(n):
#     x = input().split(" ")
#     if x[1] in k:
#         k[x[1]] += "," + x[0]
#     else:
#         k[x[1]] = x[0]
# m = int(input())
# for i in range(m):
#     t = str(input())
#     if t in k.keys():
#         print(*k[t].split(","))
#     else:
#         print("Неизвестный номер")


# n = int(input())
# k = {}
# for i in range(n):
#     x = input().split()
#     k[x[-1]] = k.get(x[-1], []) + [x[0]]
# m = int(input())
# for i in range(m):
#     t = str(input())
#     if t in k.keys():
#         print(*sorted(k[t]))
#     else:
#         print("Нет данных")


# lst = [i.split(', ') for i in iter(input, 'конец')]
# my_dict = {}
# for i in lst:
#     if i[0] not in my_dict:
#         my_dict[i[0]] = [int(i[1])]
#     else:
#         my_dict[i[0]].append(int(i[1]))
# for k, v in sorted(my_dict.items(), key=lambda x: (-(sum(x[1]) / len(x[1])), x[0])):
#     print(k, (sum(v) / len(v)))


# comments = {
#     'Дили': set(),
#     'Вили': set(),
#     'Били': set()
# }
# a = input()
# while a != 'конец':
#     name, commentator = a.split(': ')
#     comments[name].add(commentator)
#     a = input()
# for k, v in sorted(comments.items(), key=lambda item: -len(item[1])):
#     print(f'Количество уникальных комментаторов у {k} - {len(v)}')
