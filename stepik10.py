# 10.1 Генераторы и итераторы. Выражения-генераторы

# Генератор списка

# a = [i**2 for i in range(1,6)]
# print(a)
# c = (i for i in range(10000000000))

# Выражения генераторы

# for i in c:
#     print(i)
# # b = (i**2 for i in range(1,6))
# # print(sum(b))

# d = (i ** 2 for i in range(1, 6))
# print(list(d))


# # Создайте генератор
# from_10_to_20 = (i for i in range(10, 21))
#
# # Распечатайте три первых значения
# print(next(from_10_to_20))
# print(next(from_10_to_20))
# print(next(from_10_to_20))
#
# # выведите все оставшиеся
# for value in from_10_to_20:
#     print(value)


# words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon', 'drop', 'produce', 'acquisition',
#          'cheap', 'strength', 'master', 'perception', 'noise', 'strange', 'am']
#
# lens = (len(i) for i in words)
#
# for i in lens:
#     print(i)


# gen_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days = ((i, gen_days[(i+4) % 7]) for i in range(1, 78))
# for i in range(77):
#     print(next(days))


# 10.2 Функция генератор. Создание генератора при помощи yield

# def f():
#     return [43, 54, 32]
#
#
# def genf():
#     s = 7
#     for i in [43, 54, 32]:
#         yield i
#         print(s)
#         s = s*10+7
#
#
# # s = genf()
# # print(next(s))
# # print(next(s))
# # print(next(s))
#
# # for i in genf():
# #     print(i)
#
# g = genf()
# print(next(g))
# print(next(g))
# print(next(g))

# def fact(n):
#     pr = 1
#     a = []
#     for i in range(1, n+1):
#         pr = pr * i
#         a.append(pr)
#     return a
#
#
# print(fact(10))

# def fact(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr = pr * i
#         yield pr
#
#
# for i in fact(10):
#     print(i, end=' ')

# def gen_squares(n):
#     for i in range(1, n+1):
#         yield i ** 2
#
#
# for i in gen_squares(5):
#     print(i)


# def gen_fibonacci_numbers(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# for i in gen_fibonacci_numbers(10):
#     print(i)


# def my_range_gen(*args):
#     if len(args) == 1:
#         start = args[0]
#         count = 0
#         while count < start:
#             yield count
#             count += 1
#     elif len(args) == 2:
#         start, stop = args[0], args[1]
#         while start < stop:
#             yield start
#             start += 1
#     else:
#         start, stop, step = args
#         if start < stop and step > 0:
#             while start < stop:
#                 yield start
#                 start += step
#         elif start > stop and step < 0:
#             while start > stop:
#                 yield start
#                 start += step
#
#
#
# assert ([i for i in my_range_gen(5)]) == [i for i in range(5)]
# assert ([i for i in my_range_gen(4,8)]) == [i for i in range(4,8)]
# assert ([i for i in my_range_gen(4, 8, 2)]) == [i for i in range(4, 8, 2)]
# assert ([i for i in my_range_gen(8, 5, -1)]) == [i for i in range(8, 5, -1)]
# assert ([i for i in my_range_gen(20, 10, 3)]) == [i for i in range(20, 10, 3)]
# assert ([i for i in my_range_gen(1, 10, -2)]) == [i for i in range(1, 10, -2)]


# 10.3 Функция map
# class map(object)
#     map(func, *iterables) --> map object
#     Make an iterator that computes the function using arguments from
#     each of the iterables.  Stops when the shortest iterable is exhausted.

# a = [-1, 2, -3, 4, 5]
# b = list(map(abs, a))
# c = [abs(i) for i in a]
# print(b, c, sep='\n')

# def f(x):
#     return x**2
#
#
# a = [-1, 2, -3, 4, 5]
# b = list(map(f, a))
# print(b)

# a = ['hello', 'hi', 'good morning']
# b = list(map(str.upper, a))
# print(b)

# a = ['hello', 'hi', 'good morning']
# b = list(map(lambda x: x[::-1], a))
# c = [i[::-1] for i in a]
# print(b, c, sep='\n')

# a = ['hello', 'hi', 'good morning']
# b = list(map(lambda x: x + '!', a))
# print(b)

# a = ['hello', 'hi', 'good morning']
# b = list(map(list, a))
# c = list(map(sorted, b))
# print(b, c, sep='\n')

# s = list(map(int, input().split()))
# print(s)


# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609,
#            221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278,
#            118, -462, -671, 78, -69, -568, -228, -445, -47, -565]
# print(strings := list(map(str, numbers)))


# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150, -458, -372, 450, 141, -626, -168, -383, 389, -184, 609,
#            221, 311, 526, 254, -631, -174, -555, -338, 226, 695, -16, 333, 12, -600, -258, -383, -101, 121, 40, 278,
#            118, -462, -671, 78, -69, -568, -228, -445, -47, -565]
# print(increase_3 := list(map(lambda x: x*3, numbers)))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(s := list(map(lambda x: x**2, numbers)))
# print(t := list(map(lambda x: x**3, numbers)))


# def from_hex_to_rgb(color: str) -> tuple:
#     red = int(color[1:3], 16)
#     green = int(color[3:5], 16)
#     blue = int(color[5:7], 16)
#     return (red, green, blue)
#
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
#           '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
#           '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
#           '#7CFC00', '#7FFF00', '#ADFF2F']
#
# for red, green, blue in map(from_hex_to_rgb, colors):
#     print(f"Red={red}, Green={green}, Blue={blue}")


# s = input().split()
# lst = []
# for i in s:
#     up = tuple(i.upper() + i.lower())
#     lst.append(up)
# print(lst)
#
# print(list(map(lambda s: (s.upper(), s.lower()), input().split())))


# names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
#          ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
#          ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
#          ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
#          ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
#          ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
#          ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
#          ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
#          ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
#          ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
#          ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
#          ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
#          ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
#          ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
#          ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]
#
# new_names = list(map(lambda i: (i[0] + ' ' + i[1]), names))
# print(new_names)


# persons = [
#     {
#         'birthday': '1983-10-25',
#         'job': 'Field seismologist',
#         'name': 'Andrew Hernandez',
#         'phone': '680-436-8521x3468'
#     },
#     {
#         'birthday': '1993-10-03',
#         'job': 'Pathologist',
#         'name': 'Paul Harmon',
#         'phone': '602.518.4130'
#     },
#     {
#         'birthday': '2002-06-11',
#         'job': 'Designer, multimedia',
#         'name': 'Gregory Flores',
#         'phone': '691-498-5303x079'
#     },
#     {
#         'birthday': '2006-11-28',
#         'job': 'Print production planner',
#         'name': 'Jodi Garcia',
#         'phone': '(471)195-7189'},
#     {
#         'birthday': '2019-12-05',
#         'job': 'Warehouse manager',
#         'name': 'Elizabeth Cannon',
#         'phone': '001-098-434-5950x276'
#     },
#     {
#         'birthday': '1984-06-12',
#         'job': 'Visual merchandiser',
#         'name': 'Troy Lucas',
#         'phone': '+1-018-070-2288x18433'
#     },
#     {
#         'birthday': '1993-09-14',
#         'job': 'International aid/development worker',
#         'name': 'Laurie Sandoval',
#         'phone': '2930693269'
#     },
#     {
#         'birthday': '1999-05-25',
#         'job': 'Editor, film/video',
#         'name': 'Jack Clark',
#         'phone': '8643048473'
#     },
#     {
#         'birthday': '1985-09-11',
#         'job': 'Magazine journalist',
#         'name': 'Kimberly Johnson',
#         'phone': '+1-583-428-7663'
#     },
#     {
#         'birthday': '1990-10-07',
#         'job': 'Museum/gallery curator',
#         'name': 'Austin Liu PhD',
#         'phone': '714-879-5250'
#     }
# ]
# print(phones := list(map(lambda i: i['phone'], persons)))


# list_x = [25, 48, 23, 13, -18, -10, -3, 16, 2, -12, 20, -14, 14, 45, 41, 6, 11, 15, 22,
#           -14, -11, 41, 15, 48, 47, 41, -8, 1, 4, 1, 40, 27, -11, -2, -14, -15, 35, 4,
#           49, 4, 5, 13, 50, 35, -3, 3, 30, -11, 7, 12]
#
# list_y = [-9, 17, 41, 47, -5, -10, -5, 13, 31, -11, 37, 9, 46, 27, -1, 36, 32, 23, -12,
#           38, 8, 9, 17, 16, 29, -4, 4, 2, 1, 46, 6, 49, -16, 21, -19, -10, 15, -13, 20,
#           13, -18, 21, -17, 21, 10, 5, 38, -1, 18, 22]
#
# list_w = [9, -26, 3, 21, 48, -14, 43, -4, -16, 16, 41, 43, -27, -9, 10, -10, 4, -2, 1,
#           7, 30, -29, 11, 17, 31, 31, -26, 38, 38, -17, 35, 17, 35, 10, -25, 42, -30,
#           -10, -20, 20, 15, 0, 29, -30, -21, -13, -27, -21, -18, -26]
#
# print(list(map(lambda x, y, w: x**2 - x * y * w + w**4, list_x, list_y, list_w)))
