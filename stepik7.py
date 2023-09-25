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
