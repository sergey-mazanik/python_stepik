# a = 'Я стану крутым программистом!\n'
# print(a * 3)

# print('W' * 777)

# a = 'Лев Николаевич Толстой написал "Война и мир"'
# print(a)

# a = input()
# b = input()
# print(a + '\n' + b)

# a = input()
# b = input()
# c = input()
# print(c + '\n' + b + '\n' + a)

# a = input()
# print((a + ' ') * 3 + a)

# a = input()
# print(len(a))

# a = input()
# b = input()
# print(a + b)

# a = input()
# print(a * 3)

# a, b, c = map(str, input().split())
# print('Simvol code ' + a + ' is ' + str(ord(a)) + '.')
# print('Simvol code ' + b + ' is ' + str(ord(b)) + '.')
# print('Simvol code ' + c + ' is ' + str(ord(c)) + '.')

# a = input()
# print(a[0])

# a = input()
# print(a[-1])

# a = input()
# print(a[:4])

# a = input()
# print(a[-4:])

# a = input()
# print(a[::2])

# a = input()
# print(a[1::2])

# a = input()
# print(a[::-1])

# a = input()
# print(a[-1::-3])

# a = input()
# b = a[-1]
# a = b + a[:-1]
# print(a)

# a = input()
# print(a[-1] + a[:-1])

# a = input()
# print(a.upper())

# a = input()
# print(a.lower())

# s = input()
# word = input()
# print(s.lower() == word.lower())

# a = input()
# print(a[:3].upper() + a[3:-3].lower() + a[-3:].upper())

# a = input()
# print(a.swapcase())

# a = input().title()
# print(a.swapcase())

# a = input().lower()
# print(a.count('e'))

# a = input()
# print(a.find('a'))

# a = input()
# print(a.rfind('a'))

# a = input()
# print(a.replace(' ', ','))

# a = input()
# a = a.replace('w', '')
# a = a.replace('z', '')
# print(a)

# a = input().lower()
# a = a.replace('a', '')
# a = a.replace('o', '')
# a = a.replace('y', '')
# a = a.replace('e', '')
# a = a.replace('u', '')
# a = a.replace('i', '')
# a = '.'.join(a)
# print('.' + a)

# a = input().lower()
# for i in 'oayeui':
#     a = a.replace(i, '')
# a = '.'.join(a)
# print('.' + a)

# s = 'hEllO WoRlD'
# print(s.swapcase().capitalize().swapcase().lower())

# a = input()
# print(len(a.split()))

# list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
# print('-'.join(list_strings))

# a = input().lower()
# print(a.startswith('mam'))

# s = input()
# postfix = input()
# print(s.endswith(postfix))

# s = input()
# prefix = input()
# postfix = input()
# s1 = s.startswith(prefix)
# s2 = s.endswith(postfix)
# print(s1 and s2)

# a = input()
# print(a.isdigit())

# a = input()
# print(a.isupper())

# a = input()
# print(a.islower())

# a = input().ljust(15, '-')
# print(a)

# print(input().rjust(10, '!'))

# print(input().center(15, '_'))

# print(str(input().zfill(10)))

# print(input().strip('-_!?'))

# print(input().lstrip('-_!?'))

# print(input().rstrip('-_!?'))

# a = int(input())
# b = int(input())
# c = int(input())
# a1 = hex(a).upper().replace('0X', '').zfill(2)
# b1 = hex(b).upper().replace('0X', '').zfill(2)
# c1 = hex(c).upper().replace('0X', '').zfill(2)
# print('#' + a1 + b1 + c1)


# a = '''
# /\_/\
# >^,^<
#  / \
# (|_|)_/
# '''
# print(a)

# a = "  /~~~\ \n //^ ^\\\ \n(/(_*_)\) \n_/'\'*'\'\_ \n(/_)^(_\)"
# print(a)

#name = 'Семён'
# mid_name = 'Семёнов'
# balance = 32.56
# text = """Дорогой """ + name + " " + mid_name + """,
# баланс Вашего лицевого счёта составляет """ + str(balance) + """ руб."""
# print(text)

# name = 'Семён'
# mid_name = 'Семёнов'
# balance = 32.56
# text = """Дорогой {0} {1},
# баланс Вашего лицевого счёта составляет {2} руб.""".format(name, mid_name, balance)
# print(text)

# name = 'Семён'
# mid_name = 'Семёнов'
# balance = 32.56
# text = """Дорогой {name} {mid_name},
# баланс Вашего лицевого счёта составляет {balance} руб.""".format(mid_name=mid_name, name=name, balance=balance)
# print(text)

# a = input()
# print('''Что Вы сказали? {a}? Какое интересное слово'''.format(a=a))

# name = input()
# surname = input()
# print('''Здравствуйте, {name} {surname}!'''.format(name=name, surname=surname))

# a = int(input())
# prev = a - 1
# next = a + 1
# print('''Для числа {a} предыдущим будет число {prev}.
# Для числа {a} следующим будет число {next}.'''.format(a=a, prev=prev, next=next))

# name = input()
# print(f'Мое имя {name}!')

# name = input()
# age = int(input())
# print(f'Hello {name.upper()}. You are {age} years old.')

# name = input()
# year = int(input())
# print(f'{name}, вам исполнится 77 лет в {year + 77}')

# sec = int(input())
# print(f'{sec} сек - это {sec // 60} мин. {sec % 60} сек.')

# w: int = int(input())
# h = int(input())
# print(f'''Разрешение экрана: {w} x {h}.
# Общее количество пикселей = {w * h}.''')

# w, h = map(int, input().split())
# print(f'''Разрешение экрана: {w} x {h}.
# Общее количество пикселей = {w * h}.''')

# a = int(input())
# b = int(input())
# print(f'''{a} / {b} = {a / b}
# {a} // {b} = {a // b}
# {a} % {b} = {a % b}''')

# a: int = int(input())
# b: int = int(input())
# c: int = int(input())
# print(f'Vector A({a}, {b}, {c})\n'
# f'Vector B({a + 5}, {b + 5}, {c + 5})')

# currency: float = float(input())
# dollar: int = int(input())
# print(f'Current dollar rate is {currency}. You want to buy {dollar} dollars\n'
# f'You must pay {currency * dollar}')

# x: int = int(input())
# y: int = int(input())
# print(f'Точка({x = }, {y = })')

# d = 100
# print(f'{d:.1f}')
# print(f'{d:.2f}')
# print(f'{d:.3f}')

# number_pi = 3.141592653589793
# print(f'{number_pi:.6f}')

# a: float = float(input())
# print(f'{a:.2f}')

# print(f'Число\t\tКвадрат\t\tКуб')
# for x in range(1, 11):
#    print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')

# a: int = int(input())
# print(f'{a:010d}')

# APPLES = .50
# BREAD = 1.50
# CHEESE = 2.25
# num_apples = 3
# num_bread = 10
# num_cheese = 6
# price_apples = num_apples * APPLES
# price_bread = num_bread * BREAD
# price_cheese = num_cheese * CHEESE
# str_apples = 'Яблоки'
# str_bread = 'Хлеб'
# str_cheese = 'Сыр'
# total = price_bread + price_cheese + price_apples
# print(f'{"Список покупок":^30s}')
# print(f'{"=" * 30}')
# print(f'{str_apples:10s}{num_apples:10d}\t${price_apples:>5.2f}')
# print(f'{str_bread:10s}{num_bread:10d}\t${price_bread:>5.2f}')
# print(f'{str_cheese:10s}{num_cheese:10d}\t${price_cheese:>5.2f}')
# print(f'{"Total:":>20s}\t${total:>5.2f}')

# a = int(input())
# print(f'{a:-^15d}')

# text = input()
# print(f"|{text:&^20}|")
# print(f"|{text:&>20}|")
# print(f"|{text:&<20}|")

# my_list = [1]
# my_list = [1] * 77
# print(my_list)

# my_list = ['q', 'w', 't']
# my_list = my_list * 15
# print(my_list)
# print(len(my_list))

# my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# a = min(my_list)
# b = max(my_list)
# print(f'{a} {b}')

# a = list(map(int, input().split()))
# print(777 in a)

# a = list(map(int, input().split()))
# print(sum(a))

# a = list(map(int, input().split()))
# b = min(a)
# c = max(a)
# print(f'{b} {c}')

# a = list(map(int, input().split()))
# print(sum(a) / len(a))

# a = list(map(int, input().split()))
# print(a[1])

# a = list(map(int, input().split()))
# print(a[2:5])

# a = list(map(int, input().split()))
# print(a[-3:])

# a = list(map(int, input().split()))
# print(a[1::3])

# a = list(map(int, input().split()))
# print(a[::-1])

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# top[-1] = 'Сверхъестественное'
# top[2] = 'Настоящий детектив'
# print(top)

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# a = int(input())
# a = a - 1
# print(months[a])

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.extend([111, 222, 789, 201])
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.insert(5, 111)
# numbers.insert(8, 222)
# numbers.insert(0, 789)
# numbers.insert(11, 201)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
# numbers = numbers + extra
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# a = numbers.pop()
# b = numbers.pop(0)
# c = numbers.pop(12)
# d = numbers.pop(7)
# print(numbers, a + b + c + d, sep='\n')

# numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
# numbers.remove(3)
# numbers.remove(5)
# numbers.remove(7)
# numbers.remove(9)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# numbers.sort(reverse=True)
# print(numbers)

# a = list(map(int, input().split()))
# a.reverse()
# print(a)

# a = list(map(int, input().split()))
# print(a.count(999))

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# copy_numbers = numbers[:]
# print(copy_numbers)
# #or
# copy_numbers = numbers.copy()
# print(copy_numbers)

# a = input().upper()
# word1, word2 = a.split()
# list1 = list(word1)
# list2 = list(word2)
# b = "-".join(list1)
# c = "-".join(list2)
# print(b, c)
# # or
# print("-".join(list1), "-".join(list2))

# a = input().title()
# name, name2, surname = a.split()
# print(f"{surname} {name[0]}. {name2[0]}.")

# a = input()
# a = a.split()
# print('\n'.join(a))

# a = input()
# if a == 'Python':
# print('ДА')
# else:
# print('НЕТ')

# a = int(input())
# if a <= 20000:
# print(a)
# else:
# print(a * 0.87)

# a = int(input())
# b = int(input())
# if a > b:
# print(a)
# else:
# print(b)

# a, b, c = map(int, input().split())
# if a + b == c:
# print('YES')
# else:
# print('NO')

# a = list(map(int, input().split()))
# if 3 in a:
# a.remove(3)
# if 5 in a:
# a.remove(5)
# if 7 in a:
# a.remove(7)
# if 9 in a:
# a.remove(9)
#
# print(a)

# print(see_walrus := 'Look at my walrus, my walrus is amazing')
# print(see_walrus[:11] + 'horse')

# if (a := int(input())) <= 10000:
#     print(f'Сумма {a} не превышает лимит, проходите')
# else:
#     b = a - 10000
#     print(f'Ого! {a}! Куда вам столько? Мы заберем {b}')

# if 'walrus' in (a := input()):
#     print('Нашли моржа')
# else:
#     print('Никаких моржей тут нет')

# if (t := input()) == ((s := input())[::-1]):
#     print('YES')
# else:
#     print('NO')

# if (N := input()) == (N[::-1]):
#     print('YES')
# else:
#     print('NO')

# a = list(map(int, input()))
# b = a.copy()
# b.reverse()
# if a == b:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b) > c and (a + c) > b and (b + c) > a:
#     print('YES')
# else:
#     print('NO')

# a = input().zfill(6)
# sum1 = int(a[0]) + int(a[1]) + int(a[2])
# sum2 = int(a[-1]) + int(a[-2]) + int(a[-3])
# if sum1 == sum2:
#     print('YES')
# else:
#     print('NO')

# a = input()
# b = input()
# black = ['a1', 'a3', 'a5', 'a7', 'b2', 'b4', 'b6', 'b8', 'c1', 'c3', 'c5', 'c7', 'd2', 'd4', 'd6', 'd8', 'e1', 'e3',
#          'e5', 'e7', 'f2', 'f4', 'f6', 'f8', 'g1', 'g3', 'g5', 'g7', 'h2', 'h4', 'h6', 'h8']
# if ((a not in black) and (b in black)) or ((a in black) and (b not in black)):
#     print('NO')
# else:
#     print('YES')

# x = input()
# y = input()
# r =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a1 = (r.index(x[0]) + int(x[1])) % 2
# a2 = (r.index(y[0]) + int(y[1])) % 2
# if a1 == a2:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# text = 'Even' if num % 2 == 0 else 'Odd'
# print(text)

# num1 = int(input())
# num2 = int(input())
# minimum = num1 if num1 < num2 else num2
# maximum = num1 if num1 > num2 else num2
# print(f'{minimum} {maximum}')

# a = input()
# sentence = 'Вопросительное' if (a.endswith('?')) else 'Обычное'
# print(sentence)

# a = input()
# b = input()
# experiment = 'Притягиваются' if (a != b) else 'Отталкиваются'
# print(experiment)

# a = int(input())
# b = int(input())
# if a == b:
#     print('=')
# else:
#     if a > b:
#         print('>')
#     else:
#         print('<')

# a = int(input())
# b = int(input())
# c = int(input())
# if (a > b) & (a > c):
#     print(a)
# else:
#     if (b > a) & (b > c):
#         print(b)
#     else:
#         print(c)

# a, b, c = int(input()), int(input()), int(input())
# print(a if a > b and a > c else b if b > a and b > c else c)

# a = int(input())
# if a % 2 == 0:
#     print(a // 2)
# else:
#     if a == 1:
#         print(0)
#     else:
#         print(a)

# a = int(input())
# print((a // 2) if (a % 2 == 0) else 0 if (a == 1) else a)

# a, b, c = map(int, input().split())
# minimum = a if (b > a < c) else b if (a > b < c) else c
# maximum = a if (b < a > c) else b if (a < b > c) else c
# print(maximum - minimum)

# a = input().lower()
# b = input().lower()
# c = '0' if a == b else '1' if a > b else '-1'
# print(c)

# a = input().split()
# b1 = (int(a[1])*2) + int(a[3])
# b2 = (int(a[2])*2) + int(a[4])
# print('First' if b1 < b2 else 'Second' if b1 > b2 else 'Friendship')

# a = input().lower()
# b = input().lower()
# print('Good' if (a[-1] == 'ь') & (a[-2] == b[0]) else 'Good' if (a[-1] == b[0]) else 'Bad')

# a = int(input())
# if a % 3 == 0 and a % 5 == 0:
#     print('FizzBuzz')
# elif a % 3 == 0:
#     print('Fizz')
# elif a % 5 == 0:
#     print('Buzz')
# else:
#     print(a)

# a, b, c = int(input()), int(input()), int(input())
# if (a != b) & (b != c) & (a != c):
#     print(0)
# elif (a == b) & (a == c):
#     print(3)
# elif ((a == b) & (a != c)) | ((a != b) & (b == c)) | ((a == c) & (b != c)):
#     print('2')

# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# N = int(input())
# a = N - 1
# print(months[a])

# a = int(input())
# if a < 2:
#     print('Младенец')
# elif 2 <= a < 4:
#     print('Малыш')
# elif 4 <= a < 12:
#     print('Ребенок')
# elif 12 <= a < 19:
#     print('Подросток')
# elif 19 <= a < 65:
#     print('Взрослый человек')
# elif 65 <= a < 115:
#     print('Пожилой человек')

# a, b, c = float(input()), float(input()), input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '*':
#     print(a * b)
# elif (c == '/') & (b == 0):
#     print('Неизвестно')
# elif c == '/':
#     print(a / b)
# else:
#     print('Неизвестно')

# pass1 = input()
# pass2 = input()
# if len(pass1) < 7:
#     print('Short')
# elif pass1 != pass2:
#     print('Difference')
# else:
#     print('OK')

# a = int(input())
# match a:
#     case 1:
#         print("Совсем еще зеленый студентик")
#     case 2:
#         print("Джун-студент")
#     case 3:
#         print("Мидл-студент")
#     case 4:
#         print("Сеньор-студент")
#     case 5:
#         print("Босс качалки")
#     case  _:
#         print("Неизвестный курс")

# a = int(input())
# match a:
#     case 1:
#         print(31)
#     case 2:
#         print(28)
#     case 3:
#         print(31)
#     case 4:
#         print(30)
#     case 5:
#         print(31)
#     case 6:
#         print(30)
#     case 7:
#         print(31)
#     case 8:
#         print(31)
#     case 9:
#         print(30)
#     case 10:
#         print(31)
#     case 11:
#         print(30)
#     case 12:
#         print(31)
#     case _:
#         print('Error')

# match input():
#     case 'Овен' | 'Лев' | 'Стрелец':
#         print('Огненный')
#     case 'Телец' | 'Дева' | 'Козерог':
#         print('Земной')
#     case 'Близнецы' | 'Весы' | 'Водолей':
#         print('Воздушный')
#     case 'Рак' | 'Скорпион' | 'Рыбы':
#         print('Водный')
#     case _:
#         print('Error')

# a = 'privet'
# while len(a) > 0:
#     print(a[0])
#     a = a[1:]
#     print(a)









