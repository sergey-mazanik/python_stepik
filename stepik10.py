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


# 10.4 Функция filter
# filter(function or None, iterable) --> filter object
#  |
#  |  Return an iterator yielding those items of iterable for which function(item)
#  |  is true. If function is None, return the items that are true.

# def f(x):
#     return x > 10
#
#
# a = [14, 0, 5, 79, 645, 7952, 18, 0, 119, 471]
# b = list(filter(f, a))
# c = [i for i in a if i > 9 and i < 100]
# print(b, c)

# a = [14, 0, 5, '', 'hello', 7952, [], 0, 119, 471]
# b = list(filter(bool, a))
# print(b)

# a = ['world', 'hello', '3243', 'potato', 'carrot', 'hi']
# b = list(filter(lambda x: len(x) > 4, a))
# print(b)

# a = '45ojfnso23vm'
# b = list(filter(str.isupper, a))
# print(b)

# d = {
#     'moscow': 800,
#     'boston': 750,
#     'LA': 400,
#     'SF': 900,
#     'Chicago': 650,
#     'SP': 600
# }
# b = list(filter(lambda x: d[x] > 700, d))
# print(b)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 == 0, numbers)))


# numbers = [54, 71, 65, 51, 36, -82, -32, 61, -61, 92, 17, -68, -62, 40, 16, -49, -51, -38, 60, -24, -61, 3, -26, -46,
#            -97, -28, 36, 7, 52, 56, -96, -69, 67, 76, 16, 36, 38, 74, 11, -87, 69, 69, -69, -61, 92, 67, -45, -26, 94,
#            38, 27, -26, 10, 55, 28, -81, 53, -75, -32, -83, 38, 83, -40, -51, 88, 28, 76, 25, 84, -79, -69, -65, 6, 12,
#            81, -58, -92, 44, -41, 60, -14, -65, 7, 64, -40, -25, -91, -23, -19, -40, -4, 36, 38, 28, -27, -28, 72, 47,
#            -95, 47, 10, 31, 62, -75, 22, -34, 44, -62, -30, -41, 19, -13, 30, -11, -54, -46, -80, -57, -60, 72, -49, 84,
#            5, 66, 62, -35, 69, 23, 41, -15, 75, -53, 94, -76, -28, -41, -17, 71, 67, -50, 18, 65, -16, -27, -88, 21,
#            -42, 58, 85, 36, 9, -72, -26, -73, -1, 41, -87, 85, 5, -92, -60, -33, 33, -74, 17, 47, -38, -95, -39, 64, 85,
#            -27, -42, -91, -39, -15, -75, 78, -54, 26, -10, -3, 89, -11, -71, -85, 63, 9, -59, 72, 27, 40, 99, -9, 77,
#            64, -39, -28, 73, -50, -80, -74, 52, 26, 53, -18, 22, 70, 85, 1, -90, 53, -19, -80, -14, -29, -64, -21, 23,
#            99, 15, -52, 66, 30, 82, -81, -30, -68, 30, -25, -63, 33, 1, 0, 84, 18, -35, 31, -34, 10, 48, -37, -41, -94,
#            -1, -14, -87, -37, -6, 48, 38, 33, -13, 71, -81, 45, -63, 52, -35, 34, -88, -82, -7, -92, -22, 96, -28, 0,
#            21, 74, -28, 81, 81, 44, -16, 17, -95, 18, -73, 15, -61, 6, -43, -67, -31, -61, -72, -66, 60, 67, -13, 47,
#            29, 44, -93, 55, -13, -23, 74, 79, 32, -20, 33, 17, -48, 7, 24, 19, 89, -60, 34, 81, 18, -39, 56, 10, -32,
#            46, -33, -75, -99, -37, -23, 59, -33, -1, 75, -65, 92, 80, 51, -59, -28, -22, -47, -1, 28, -85, 1, 23, -15,
#            -66, -97, -25, 7, 17, -87, -60, 14, -70, 88, 20, 40, -89, 38, -41, -97, 76, 80, 43, 22, -72, -38, 47, -2, 12,
#            58, -91, 82, -98, 50, 15, -33, -56, 69, -27, 94, -90, 92, -71, -73, -71, -78, 22, -86, -48, 10, 46, 19, 68,
#            -23, 52, -42, 74, 44, 89, -71, 93, 43, -86, 79, 3, -56, 14, 41, 15, -37, 77, -9, 36, 51, -89, 1, 37, 82, 27,
#            72, -92, 91, 94, 71, -81, -49, -42, 26, 57, -30, -40, 86, -77, -85, 1, 71, 16, 73, -82, 26, -90, 72, 14, -65,
#            -55, 34, 45, 66, -64, -40, 92, 42, -78, -22, 53, -18, -41, -75, 10, -59, -55, 8, -90, -3, -65, 43, -49, -86,
#            -96, 69, 48, 27, -48, -42, -34, -6, 7, 50, -55, -65, 79, 30, 16, -21, -98, -73, -25, -20, -51, 20, 17, -91,
#            34, 96, 12, 13, -58, -73, -82, 19, -48, -61, 57, 96, 74, 34, -63, 38, -27, -12, -24, 94, -25, -10, -41, 53,
#            -13, 16, -21, 24, 96, 95, 58, 83, 10, 42, -11, -33, 10, 38, -6, -66, -40, -36, -99, -55, 37, -81, -93, 67,
#            -77, -3, 77, 25, 38, -16, 21, -82, 77, 95, 73, 9, 94, -27, -21, -33, -90, 31, 98, 28, -63, 75, 53, -17, -1,
#            6, 51, 11, -92, 30, -24, 12, 47, -75, -15, -63, 57, 3, 37, -82, -28, -26, -3, -30, -90, -45, 20, -41, 72,
#            -42, 15, -3, 92, 57, -1, 40, -65, 88, 28, -76, 52, -63, -51, 59, 69, -39, -47, -1, -18, -57, 68, 77, 66, 62,
#            -71, 31, -50, 61, 88, 98, 5, 98, -57, -46, 2, 90, 43, 67, 76, -81, -57, 77, 25, -66, -81, -92, -76, 72, 14,
#            59, 52, 36, 20, -2, 92, 58, 36, -34, 94, -74, 42, -56, 96, -81, 69, -83, 71, -13, -13, 56, 86, -29, 58, -17,
#            65, 70, 74, 28, 8, 91, 51, 79, -57, -86, 5, -37, -67, -28, 56, 65, -90, 97, -20, 81, -85, -45, 46, -74, 76,
#            -75, -7, 74, 82, 56, 14, -43, 20, -48, -99, 19, -39, -66, 44, -75, 24, -5, -70, 85, -12, 20, -85, -69, -26,
#            -57, 28, -96, 42, -56, 13, 80, -48, 59, 11, -30, 4, -96, 58, 41, -2, -84, -51, 52, -69, 37, 60, -12, 48, -5,
#            -48, 29, -62, 42, 15, 16, 65, 60, 43, -53, 4, 50, -21, 1, -21, -42, -57, -21, -50, -67, 77, -22, -5, 59, -67,
#            86, -77, 39, -67, 41, 83, -21, 33, 73, 55, 80, 93, 44, -71, 38, -93, 4, 83, -52, 75, -51, 1, -11, -45, 56,
#            81, 84, 70, 23, -36, -63, 69, 1, 86, -21, 53, -85, 70, -89, -31, -10, -94, -76, -17, -21, -60, 49, -22, -48,
#            67, 21, 18, 89, 20, 73, -43, -17, -52, 36, -21, 6, -37, -98, 94, 56, 31, 99, 86, 65, -19, -67, 46, 20, -29,
#            -88, -54, 88, -12, -69, 17, 83, -94, 21, 59, -99, 70, -54, -35, 2, 58, 93, 1, -35, -44, 47, 40, 55, 10, -15,
#            -96, -42, 10, -83, -82, -26, 48, 78, -72, 56, -99, -36, 25, 76, -3, -95, -38, -24, 96, 82, 7, 84, 46, 8, 93,
#            -52, -86, 87, -85, -81, 52, -67, 52, -45, -93, -69, 60, -83, -20, -14, 80, -36, 62, -78, 3, -61, 51, 48, 73,
#            92, -65, 71, -86, 8, -14, 82, 58, -58, -21, 62, -38, 16, 20, -80, -78, 19, 19, 93, -83, 2, 71, 85, 71, -4,
#            81, 4, 90, 73, 21, -3, -55, 49, 66, -4, -6, 42, 76, -3, -94, 49, 55, -53, 12, 1, -25, 56, 93, -68, -21, 15,
#            -13, 35, 71, -68, 34, -44, 48, 97, 51, 32, 87, 27, -85, -41, -27, 54, -91, -99, 83, -44, 70, -87, -76, 49,
#            99, 38, 15, 75, -54, -59, 22, 80, 49, -63, 8, -46, 97, -4, -92, -47, -20]
# a = list(filter(lambda x: x < 0, numbers))
# b = list(filter(lambda x: x == 0, numbers))
# c = list(filter(lambda x: x > 0, numbers))
# print(f'{len(a)} {len(b)} {len(c)}')


# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# a = list(filter(lambda x: len(x) == 4 or x.startswith('S'), days))
# a = sorted(a)
# print(*a, sep='\n')


# 10.5 Функция zip

# a = [5, 6, 7, 8]
# b = [100, 200, 300, 40]
# c = 'fndd'
#
# for i in range(4):
#     print(a[i], b[i])
# rez = zip(a, b, c)
# print(list(rez))

# rez = zip(a, b, c)
# col1, col2, col3 = zip(*rez)
# print(col1, col2, col3)


# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y, strict=True)
# result = list(zipped)
# print(result)


# keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
# values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(dict(zip(keys, values)))


# employees = [
#     'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
#     'Leonti', 'Daniil', 'Mishka', 'Lidochka',
#     'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
# ]
# identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]
#
# employees_data = dict(zip(sorted(identifiers), sorted(employees)))
# print(employees_data)


# # Напишите определение функции zip_with_function
# def zip_with_function(lst, func):
#     return list(map(lambda args: func(*args), zip(*lst)))
#
#
# def combine_strings(a: str, b: str) -> str:
#     return a + b
#
#
# def get_sum_two_numbers(a: int, b: int) -> int:
#     return a + b
#
#
# def get_sum_three_numbers(a: int, b: int, c: int) -> int:
#     return a + b + c
#
#
# assert zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers) == [4, 7, 12]
# assert zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers) == [40, 20]
# assert zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers) == [10, 15, 20]
# assert zip_with_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]], get_sum_three_numbers) == [12, 15, 18]
# assert zip_with_function([["a", "b"], ["1", "2"]], combine_strings) == ['a1', 'b2']
