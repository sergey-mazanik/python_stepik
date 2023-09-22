# a = 1000
# while a <= 2000:
#     print(a)
#     a += 1

# a = 6785
# while (a >= 195) & (a % 5 == 0):
#     print(a)
#     a -= 5

# a, b = map(int, input().split())
# i = 0
# while a <= b:
#     a = a * 3
#     b = b * 2
#     i += 1
# print(i)

# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6,
#            6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9,
#            2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4,
#            8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5,
#            6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2,
#            4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers:
#     numbers.remove(4)
# print(*numbers)

# a = input()
# while len(a) >= 1:
#     print(a)
#     a = a[1:-1]

# a = int(input())
# b = 1
# c = 0
# while a >= (b ** 2):
#     c = b ** 2
#     b += 1
#     print(c)

# X, Y = map(int, (input().split()))
# i = 1
# while X <= Y:
#     X *= 1.15
#     i += 1
# print(i)

# n, m = map(int, input().split())
# d = 0
# while n > 0:
#     n -= 1
#     d += 1
#     if d % m == 0:
#         n += 1
# print(d)

# a, b = map(int, input().split())
# h = 0
# while a > 0:
#     a -= 1
#     h += 1
#     if h % b == 0:
#         a += 1
# print(h)

# a = int(input())
# s = 0
# while (2 ** s) < a:
#     s += 1
# if 2 ** s == a:
#     print(s)
# else:
#     print('НЕТ')

# a = int(input())
# b = int(str(a)[0])
# while (a <= 1000000000) & (b != 1):
#     a = a * b
#     b = int(str(a)[0])
# print(a)

# a = []
# while 0 not in a:
#     b = int(input())
#     a.append(b)
# print(sum(a))

# a = input()
# b = ''
# while 5 <= len(a) <= 9:
#     b = a
#     a = input()
#     if 5 <= len(a) <= 9:
#         b = a
#     else:
#         break
# print(b)

# a = int(input())
# b = []
# while sum(b) <= a:
#     c = int(input())
#     if (sum(b) + c) <= a:
#         b.append(c)
#     else:
#         break
# print(f'Довольно!\n{sum(b)}\n{len(b)}')

# n, k = map(int,input().split())
# d = 240 - k
# i = 5
# level = 1
# summa = 0
# count = 0
# while summa < d and n != 0:
#     n -= 1
#     level += 1
#     i = level * 5
#     summa += i
#     count += 1
# print(count)

# n = int(input())
# level = 0
# cub_level = 0
# s = 0
# while s < n:
#     level += 1
#     cub_level += level
#     s += cub_level
# if s == n:
#     print(level)
# else:
#     print(level - 1)

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = []
# i = j = 0
# while i < n and j < m:
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1
# while i < n:
#     c.append(a[i])
#     i += 1
# while j < m:
#     c.append(b[j])
#     j += 1
# for i in c:
#     print(i, end=' ')

# n = int(input())
# boys = list(map(int, input().split()))
# m = int(input())
# girls = list(map(int, input().split()))
# boys.sort()
# girls.sort()
# i = j = 0
# count = 0
# while i < n and j < m:
#     if abs(boys[i] - girls[j]) <= 1:
#         count += 1
#         i += 1
#         j += 1
#     elif boys[i] < girls[j]:
#         i += 1
#     else:
#         j += 1
# print(count)

################################################################################################

# a = int(input())
# while a > 0:
#     b = a % 10
#     print(b)
#     a //= 10

# a = int(input())
# b = []
# while a > 0:
#     last = a % 10
#     b.append(last)
#     a //= 10
# print(sum(b))

# a = int(input())
# b = 1
# while a > 0:
#     last = a % 10
#     b = b * last
#     a //= 10
# print(b)

# a = int(input())
# mini = 9
# maxi = 0
# while a > 0:
#     last = a % 10
#     if last > maxi:
#         maxi = last
#     if last < mini:
#         mini = last
#     a = a // 10
# print(f'{mini}\n{maxi}')

# a = int(input())
# count = 0
# while a > 0:
#     last = a % 10
#     if last == 7:
#         count = count + 1
#     a //= 10
# print(count)

# a = int(input())
# while a > 0:
#     last = a % 2
#     print(last)
#     a //= 2

#Поиск делителя - медленный вариант на больших числах
#n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=' ')
#     i += 1

#Поиск делителя - чуть быстрее вариант
#n = int(input())
# i = 1
# while i <= n // 2:
#     if n % i == 0:
#         print(i, end=' ')
#     i += 1

#Поиск делителя - оптимальный вариант
# n = int(input())
# i = 1
# a = []
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# a.sort()
# print(a)

# n = int(input())
# i = 1
# a = []
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# if len(a) == 2:
#     print('Yes')
# else:
#     print('No')

# n = int(input())
# i = 1
# a = []
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# print(sum(a))

# Наибольший общий делитель путем вычитания
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(f'Нод={a}')

# Наибольший общий делитель путем деления
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# while b > 0:
#     c = a%b
#     a = b
#     b = c
# print(f'Нод={a}')

# Наибольшее общее кратное
# a, b = map(int, input().split())
# d = a * b
# while b > 0:
#     c = a%b
#     a = b
#     b = c
# print(d // a)

# Break
# a = 1
# while a > 0:
#     print(a)
#     if a == 5:
#         break
#     a += 1

# Continue
# a = 0
# while a <= 10:
#     a += 1
#     if a % 2 != 0:
#         continue
#     print(a)

# Else
# a = [24, 68, 42, 32, 18, 22]
# while len(a) > 0:
#     last = a.pop()
#     if last % 2 != 0:
#         print('No')
#         break
#     print(f'{last} четное число')
# else:
#     print('Yes')

# n = int(input())
# i = 1
# a = []
# while i * i <= n:
#     if n % i == 0:
#         a.append(i)
#         if i != n // i:
#             a.append(n // i)
#     i += 1
# a.sort()
# print(a[1])

# n = int(input())
# i = 2
# while i <= n:
#     if n % i == 0:
#         print(i)
#         break
#     i += 1

# a = int(input()) - 1
# b = int(input())
# while a < b:
#     a += 1
#     if a % 777 == 0:
#         break
#     if (a % 2 == 0) | (a % 3 == 0):
#         continue
#     print(a)

# a = int(input())
# count = 0
# while a > 0:
#     if a == 1:
#         break
#     if a % 2 == 0:
#         count += 1
#         a = a // 2
#         continue
#     if a % 2 != 0:
#         count += 1
#         a = a * 3 + 1
#         continue
#     a -= 1
# print(count)

# a = input()
# ind = 0
# while ind < len(a):
#     if a[ind] == 'e' or a[ind] == 'a':
#         print(f'Ага! Нашлась')
#         break
#     else:
#         print(f'Текущая буква: {a[ind]}')
#         ind += 1
#         continue
# else:
#     print('Распечатали все буквы')







