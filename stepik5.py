# n = int(input())
# for i in range(1, n+1):
#     print(i)

# for i in range(0, 501, 5):
#     print(i)

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# for i in range(13):
#     print('Надо было брать биткоин в 2012!')

# phr = input()
# n = int(input())
# for i in range(n):
#     print(phr)

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if (i % 3 == 0) & (i % 5 == 0):
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     print(f'Число {i}; его квадрат = {i * i}; его куб = {i ** 3}')

# n = int(input())
# summa = 0
# for i in range(n):
#     if (i % 3 == 0) | (i % 5 == 0):
#         summa += i
# print(summa)

# summa = 0
# for i in range(50, 101):
#     cube = i ** 3
#     summa = summa + cube
# print(summa)

# n = int(input())
# a = 1
# if n == 0:
#     print(1)
# elif n == 1:
#     print(1)
# else:
#     for i in range(2, n + 1):
#         a = a * i
#     print(a)

# n = int(input())
# mishka = 0
# chris = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     if a > b:
#         mishka += 1
#     elif a < b:
#         chris += 1
#     else:
#         continue
# if mishka > chris:
#     print('Mishka')
# elif mishka < chris:
#     print('Chris')
# else:
#     print('Friendship is magic!^^')
# # print('Mishka' if x > y else 'Chris' if x < y else 'Friendship is magic!^^')

# n = int(input())
# for i in range(n):
#     s = input().lower()
#     if 'рок' in s:
#         print(i + 1, s.find('рок') + 1)

# n = int(input())
# a = []
# for i in range(n):
#     s = input().lower()
#     if 'соль' not in s:
#         a.append(s)
# print(', '.join(a))

# n = int(input())
# for i in range(n):
#     s = input()
#     if len(s) <= 10:
#         print(s)
#     else:
#         print(f'{s[0]}{len(s) - 2}{s[-1]}')

# numbers = [99, 50, -16, 9, 47, -62, 5, -64, -68, 85, 11, -20, 16, 96, -43, 46, -25, 33, 81, -30, 64, 66, -11, 60, 3, -5, -1,
#  -80, 49, -12, -86, -40, -98, -92, -91, -71, 56, -76, -30, -82, 17, -2, -64, 47, 22, -28, 40, 55, 54, -3, -58, -10,
#  -35, -15, -2, -60, 70, 50, -77, 83, -49, 42, 27, -58, -79, -2, -100, -42, -18, 38, 95, 9, 98, -89, -46, 96, 64,
#  -35, 41, 94, 1, -90, 29, 23, 39, -3, 11, -65, -64, 52, -69, 32, -14, -49, -28, -11, 85, -75, -6, 15]
# for i in range(len(numbers)):
#     print(numbers[i])

# words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
#            'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
#            'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
#            'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
#            'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
#            'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
#            'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
#            'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
#            'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']
# for i in range(len(words)):
#     if len(words[i]) > 6:
#         print(words[i])

# numbers = [-35, 68, -91, 23, -92, -82, -74, 32, 39, -30, -100, -29, 54, 26, 54, -45, 20, 53, -17, 68, -35, 11, 26, -17,
#            70, 89, -81, -4, 61, -45, 13, 63, -48, -66, -92, -15, -88, -87, -75, 44, -49, -81, 19, -33, -59, 85, -69,
#            -60, 9, -98, 28, 11, 15, -35, -80, 5, -20, -52, -45, 26, 47, -16, 40, -14, -12, 15, 73, -16, 29, -98, 93,
#            -77, 1, 85, 77, 73, 100, -71, 99, 39, 2, -38, 49, -31, 15, 43, 94, -39, -89, -46, -71, 39, -56, 41, -93, 4,
#            -79, 48, 88, -51]
# for i in range(len(numbers)):
#     numbers[i] *= 2
# print(numbers)

# a = int(input())
# b = []
# for i in range(a):
#     name = input()
#     b.append(name)
# print(b)

# letterLow = input()
# letterUp = letterLow.upper()
# sentence = input().split()
# for i in range(len(sentence)):
#     if (letterLow in sentence[i]) | (letterUp in sentence[i]):
#         print(sentence[i])

# lst = list(map(int, input().split()))
# num = int(input())
# count = 0
# for i in range(len(lst)):
#     count += 1
#     if lst[i] == num:
#         print(count)
#         break
# else:
#     print('ErrorValue')

# lst = list(map(int, input().split()))
# lst1 = []
# for i in range(len(lst)):
#     if lst[i] > 0:
#         lst1.append(lst[i])
# lst1.sort()
# if len(lst1) != 0:
#     print(lst1[0])
# else:
#     print('Empty')

# word = input().lower()
# lst = []
# for i in range(len(word)):
#     lst.append(word.count(word[i]))
# print(max(lst))

# num = input()
# chet = []
# nechet = []
# for i in range(len(num)):
#     if i % 2 == 0:
#         chet.append(int(num[i]))
#     else:
#         nechet.append(int(num[i]))
# print('YES' if ((sum(chet) - sum(nechet)) % 11 == 0) else 'NO')

# sent = input()
# num = []
# for i in range(len(sent)):
#     if sent[i].isdigit():
#         num.append(int(sent[i]))
# print(f'{len(num)} {sum(num)}')

# bracket = input()
# openBr = []
# closeBr = []
# for i in range(len(bracket)):
#     if '(' == bracket[i]:
#         openBr.append(i)
#     elif ')' == bracket[i]:
#         closeBr.append(i)
# if (bracket[0] == ')') | (len(openBr) != len(closeBr)):
#     print('NO')
# else:
#     print('YES')

# bracket = input()
# count = 0
# for i in range(len(bracket)):
#     if count < 0:
#         break
#     elif bracket[0] == ')':
#         count = -1
#     elif bracket[i] == '(':
#         count += 1
#     else:
#         count -= 1
# if count == 0:
#     print('YES')
# else:
#     print('NO')

# bracket = input()
# count = 0  # ()
# count1 = 0  # []
# count2 = 0  # {}
# for i in range(len(bracket)):
#     if count < 0 | count1 < 0 | count2 < 0:
#         break
#     elif (bracket[0] == ')') | (bracket[0] == ']') | (bracket[0] == '}'):
#         count = count1 = count2 = -1
#     elif bracket[i] == '(':
#         count += 1
#     elif bracket[i] == ')':
#         count -= 1
#     elif bracket[i] == '[':
#         count1 += 1
#     elif bracket[i] == ']':
#         count1 -= 1
#     elif bracket[i] == '{':
#         count2 += 1
#     elif bracket[i] == '}':
#         count2 -= 1
# if count == 0 & count1 == 0 & count2 == 0:
#     print('YES')
# else:
#     print('NO')

# bracket = input()
# stack = []
# is_good = True
# for i in bracket:
#     if i in '([{':
#         stack.append(i)
#     elif i in ')]}':
#         if not stack:   # вернёт False, если в stack пусто
#             is_good = False
#             break
#         openBracket = stack.pop()
#         if openBracket == '(' and i == ')':
#             continue
#         if openBracket == '{' and i == '}':
#             continue
#         if openBracket == '[' and i == ']':
#             continue
#         is_good = False
#         break
# if is_good and len(stack) == 0:
#     print('YES')
# else:
#     print('NO')

# sent = input().split()
# res = []
# res1 = []
# for i in sent:
#     if i.lower() not in res:
#         res.append(i.lower())
#         res1.append(i)
# print(' '.join(res1))

# n = int(input())
# a = [0] * 10
# for i in str(n):
#     digit = int(i)
#     a[digit] += 1
# for i in range(10):
#     if a[i] > 0:
#         print(i, a[i])

# n = int(input())
# lst = list(map(int, input().split()))
# count = [0] * 201
# for i in lst:
#     count[i] += 1
# for i in range(-100, 101):
#     if count[i] > 0:
#         print((str(i) + ' ') * count[i], end='')

# s = 0
# for i in range(1000, 10000):
#     x = 0
#     for j in str(i):
#         x += int(j)
#     if x == 20:
#         s += i
# print(s)

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(j + 1, end=' ')
#     print()

# lst = list(map(int, input().split()))
# for i in range(len(lst)):
#     print('*' * int(lst[i]))

# lst = list(map(int, input().split()))
# for i in lst:
#     for j in range(i):
#         print('*', end='')
#     print()

# n = int(input())
# count = 0
# for p in range(n + 1, 2 * n):
#     if p % 2 == 0 and p != 2 or p == 1:
#         continue
#     d = 3
#     is_plain = True
#     while d * d <= p:
#         if p % d == 0:
#             is_plain = False
#             break
#         d += 2
#     if is_plain:
#         count += 1
# print(count)

# def is_plain_number(p):
#     if p % 2 == 0 and p != 2 or p == 1:
#         return False
#     d = 3
#     while d * d <= p:
#         if p % d == 0:
#             return False
#         d += 2
#     return True
#
# n = int(input())
# count = 0
# for p in range(n + 1, 2 * n):
#     if is_plain_number(p):
#         count += 1
# print(count)

# n = int(input())
# lst = list(map(int, input().split()))
# count = 0
# for j in range(n - 1):
#     for i in range(n - 1):
#         if lst[i] > lst[i + 1]:
#             count += 1
#             lst[i], lst[i + 1] = lst[i + 1], lst[i]
# print(*lst)
# print(count)

# n, m = map(int, input().split())
# count = 0
# a = 0
# while a ** 2 <= n:
#     b = n - a ** 2
#     if b >= 0 and a + b ** 2 == m:
#         count += 1
#     a += 1
# print(count)

# a = int(input())
# lst = list(map(int, input().split()))
# for i in range(a):
#     for j in range(i, 0, -1):
#         if lst[j] < lst[j-1]:
#             lst[j], lst[j-1] = lst[j-1], lst[j]
#         else:
#             break
# print(*lst)

# n = int(input())
# matrix = []
# summa = 0
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if j == i:
#             summa += matrix[i][j]
# print(summa)

# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# for column in range(n):
#     for row in range(n):
#         print(matrix[row][column], end=' ')
#     print()

# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# for column in range(n-1, -1, -1):
#     for row in range(n-1, -1, -1):
#         print(matrix[row][column], end=' ')
#     print()

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for row in range(n):
#     for column in range(m-1, -1, -1):
#         print(matrix[row][column], end=' ')
#     print()

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for row in range(n-1, -1, -1):
#     for column in range(m):
#         print(matrix[row][column], end=' ')
#     print()

# matrix = []
# for i in range(5):
#     matrix.append(list(map(int, input().split())))
#
# for i in range(5):
#     for j in range(5):
#         if matrix[i][j] == 1:
#             row = i
#             column = j
#
# print(abs(2 - row) + abs(2 - column))

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# for row in range(n):
#     sumRow = 0
#     for column in range(m):
#         sumRow += matrix[row][column]
#     print(sumRow, end=' ')
# print()
# for column in range(m):
#     sumColumn = 0
#     for row in range(n):
#         sumColumn += matrix[row][column]
#     print(sumColumn, end=' ')

# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# count = 0
# sumUp = 0
# sumDown = 0
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         elif matrix[i][j] != matrix[j][i]:
#             count += 1
# if count > 0:
#     print('No')
# else:
#     print('Yes')

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# win = 0
# summa = 0
# for i in range(n):
#     sumRow = 0
#     for j in range(m):
#         sumRow += matrix[i][j]
#     if sumRow > summa:
#         summa = sumRow
#         win = i
# print(summa, win, sep='\n')

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# maximum = 0
# row = 0
# column = 0
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > maximum:
#             maximum = matrix[i][j]
#             row = i
#             column = j
# print(f'{maximum}\n{row} {column}')

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# max_score = 0
# max_summa = 0
# max_index = 0
# for i in range(n):
#     maximum = 0
#     s = 0
#     for j in range(m):
#         s += matrix[i][j]
#         if matrix[i][j] > maximum:
#             maximum = matrix[i][j]
#     if maximum > max_score:
#         max_score = maximum
#         max_summa = s
#         max_index = i
#     elif maximum == max_score and s > max_summa:
#         max_score = maximum
#         max_summa = s
#         max_index = i
# print(max_index)

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# maximum = 0
# count = 0
# for i in range(n):
#     local_max = 0
#     for j in range(m):
#         if matrix[i][j] > local_max:
#             local_max = matrix[i][j]
#     if local_max > maximum:
#         maximum = local_max
#         count = 1
#     elif local_max == maximum:
#         count += 1
# print(count)

# n, m = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
#
# maximum = 0
# count = 0
# for i in range(n):
#     local_max = max(matrix[i])
#     if local_max > maximum:
#         maximum = local_max
#         count = 1
#     elif local_max == maximum:
#         count += 1
# print(count)

# matrix = []
# for i in range(4):
#     matrix.append(input())
#
# is_sim = True
# for i in range(len(matrix) - 1):
#     for j in range(len(matrix) - 1):
#         if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
#             is_sim = False
#             print('No')
#             break
# if is_sim:
#     print('Yes')

# n, m = map(int, input().split())
# matrix1 = []
# for i in range(n):
#     matrix1.append(list(input()))
# input()
# matrix2 = []
# for i in range(n):
#     matrix2.append(list(input()))
# count = 0
# for row in range(n):
#     for col in range(m):
#         if matrix1[row][col] == matrix2[row][col]:
#             count += 1
# print(count)

# n, x = map(int, input().split())
# count = 0
# i = 1
# while i * i <= x:
#     if x % i == 0 and i <= n and x // i <= n:
#         if i != x // i:
#             count += 2
#         else:
#             count += 1
#     i += 1
# print(count)

# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, input().split())))
# maxi = 0
# x = -1
# for row in range(n):
#     if matrix[row][x] > maxi:
#         maxi = matrix[row][x]
#     x -= 1
# print(maxi)

# n = int(input())
# a, b, c = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append([0] * n)
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             matrix[i][j] = c
#         elif i > j:
#             matrix[i][j] = b
#         else:
#             matrix[i][j] = a
# for i in matrix:
#     print(*i)

# n = int(input())
# commands = []
# for i in range(n):
#     home, guest = map(int, input().split())
#     commands.append([home, guest])
# count = 0
# for i in range(n-1):
#     for j in range(i + 1, n):
#         if commands[i][0] == commands[j][1]:
#             count += 1
#         if commands[i][1] == commands[j][0]:
#             count += 1
# print(count)

# class Team:
#
#     def __init__(self, h, g):
#         self.home = h
#         self.guest = g
#
# n = int(input())
# commands = []
# for i in range(n):
#     home, guest = map(int, input().split())
#     commands.append(Team(home, guest))
# count = 0
# for i in range(n-1):
#     for j in range(i + 1, n):
#         if commands[i].home == commands[j].guest:
#             count += 1
#         if commands[i].guest == commands[j].home:
#             count += 1
# print(count)

# n, m = map(int, input().split())
# mas = []
# mas.append('.' * (m + 2))
# for i in range(n):
#     row = '.' + input() + '.'
#     mas.append(row)
# mas.append('.' * (m + 2))
# k = 0
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if mas[i - 1][j] == '.' and mas[i][j + 1] == '.'  and mas[i + 1][j] == '.' and mas[i][j - 1] == '.' and mas[i][j] == '.':
#             k += 1
# print(k)

#for i in range(n):
#     triangle.append([1] + [0] * m)
# for i in range(1):
#     for j in range(m+1):
#         triangle[i][j] = 1

# n, m = map(int, input().split())
# triangle = []
# for i in range(n):
#     triangle.append(list(map(int, input().split())))
#
# for i in range(1, n):
#     for j in range(1, m):
#         triangle[i][j] = triangle[i-1][j] + triangle[i][j-1]
#
# for i in range(n):
#     for j in range(m):
#         print(triangle[i][j], end=" ")
#     print()

# n, m = map(int, input().split())
# triangle = []
# for i in range(n):
#     triangle.append(list(map(int, input().split())))
#
# for i in range(n - 2, -1, -1):
#     for j in range(m - 2, -1, -1):
#         triangle[i][j] = triangle[i + 1][j] + triangle[i][j + 1]
#
# for i in range(n):
#     for j in range(m):
#         print(triangle[i][j], end=" ")
#     print()

# n, m = map(int, input().split())  # ввод строки/стобцы
# u = 0  # счетчик
#
# for i in range(n):  # цикл строка
#     a = []  # список для строки
#     for j in range(m):  # цикл столбцы в строке
#         a.append(u)  # добавляем в список число
#         u += 1  # к числу прибавляем +1
#
#     # сразу же в этом цикле печатаем матрицу
#     if i % 2 != 0:  # если не четная строка
#         a.reverse()  # переворачиваем список
#     if i == 0:
#         print(*a, sep=2 * ' ')  # для 0 строки 2 пробела
#     else:
#         print(*a)

# n, m = map(int, input().split())
# matrix = []
# is_color = False
# for i in range(n):
#     matrix.append(list(map(str, input().split())))
#
# for i in range(n):
#     for j in range(m):
#         if 'C' in matrix[i][j] or 'M' in matrix[i][j] or 'Y' in matrix[i][j]:
#             is_color = True
#             break
#         else:
#             is_color = False
# if is_color:
#     print('#Color')
# else:
#     print('#Black&White')

# n = int(input())
# mas = [[0] * n for i in range(n)]
# i = 1
# x = 0
# y = -1
# d_row = 0 # -1 or 0 or 1
# d_col = 1 # -1 or 0 or 1
# length = len(str(n ** 2))
# while i <= n ** 2:
#     if 0 <= x + d_row < n and 0 <= y + d_col < n and mas[x + d_row][y + d_col] == 0:
#         x += d_row
#         y += d_col
#         mas[x][y] = i
#         i += 1
#     else:
#         if d_col == 1:
#             d_col = 0
#             d_row = 1
#         elif d_row == 1:
#             d_row = 0
#             d_col = -1
#         elif d_col == -1:
#             d_col = 0
#             d_row = -1
#         elif d_row == -1:
#             d_row = 0
#             d_col = 1
#
# for row in mas:
#     for elem in row:
#         print(str(elem).rjust(length), end=' ')
#     print()

# r, c = map(int, input().split())
# tort = []
# for i in range(r):
#     tort.append(input())
# mas = [[False] * c for i in range(r)]
# for i in range(r):
#     if 'S' not in tort[i]:
#         for j in range(c):
#             mas[i][j] = True
# for j in range(c):
#     is_find = False
#     for i in range(r):
#         if tort[i][j] == 'S':
#             is_find = True
#             break
#     if not is_find:
#        for i in range(r):
#            mas[i][j] = True
# count = 0
# for row in mas:
#     count += row.count(True)
# print(count)

# zeroes = [0 for i in range(10)]
# print(zeroes)

# a = [i for i in range(1, (int(input())) + 1)]
# print(a)

# n = int(input())
# a = [i for i in range(1, n+1) if n % i == 0]
# print(a)

# n = int(input())
# a = [i + 1 for i in range(n-1, n * n) if i % 2 == 0]
# print(a)

# a, b = map(int, input().split())
# a = [i ** 2 if a <= b else i ** 3 for i in (range(a, b + 1) if a <= b else range(a, b - 1, -1))]
# print(a)

# st = 'Create a list of the first letters of every word in this string'
# st = st.split()
# print([i[0] for i in st])

# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print([ascii_uppercase[i] for i in range(int(input()))])

# from string import ascii_uppercase
# print([ascii_uppercase[i-1] * i for i in range(1, int(input()) + 1)])

# phrase = 'Take only the words that start with t in this sentence'
# phrase = phrase.split()
# print([phrase[i] for i in range(len(phrase)) if 't' == phrase[i][0] or 'T' == phrase[i][0]])
