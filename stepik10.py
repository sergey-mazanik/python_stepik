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
