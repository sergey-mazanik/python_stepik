# import os
# print(os.name)
# print(os.environ)

# from string import Template
# values = {'one': 'Привет', 'copter': 'Квадракоптер'}
#
# t = Template("""
# Ну что, мои хорошие, всем $one
# Это шаблонная строка
# В нее можно вставлять значения по ключам
# Хочу сюда вставлю слово $copter, хочу сюда $copter
# """)
#
# print(t.substitute(values))

# import sys
# print(sys.getrecursionlimit())

# from string import ascii_lowercase, ascii_uppercase, punctuation
# print(punctuation, ascii_uppercase, ascii_lowercase, sep='\n')

# ____________________________ UNIT_9 ______________________________

# def file_read(file_name: str) -> None:
#     f = open(file_name, 'r', encoding='utf-8')
#     text = f.read()
#     print(text)
#     f.close()

# def file_n_lines(file_name: str, n: int) -> None:
#     f = open(file_name, 'r', encoding='utf-8')
#     for row in range(n):
#         print(f.readline(), end='')
#     f.close()

# def create_file_with_numbers(n: int) -> None:
#     f = open(f'range_{n}.txt', 'w', encoding='utf-8')
#     for row in range(1, n+1):
#         f.writelines(f'{row}\n')
#     f.close()
#
#
# create_file_with_numbers(5)

# from string import punctuation
#
#
# def remove_punctuation(word):
#     for punc in punctuation:
#         if punc in word:
#             word = word.replace(punc, '')
#     return word
#
#
# def longest_word_in_file(file_name: str) -> str:
#     file = open(file_name, 'r', encoding='utf-8')
#     max_word = ''
#     for line in file:
#         words = line.split()
#         for word in words:
#             word_without_punc = remove_punctuation(word)
#             if len(word_without_punc) >= len(max_word):
#                 max_word = word_without_punc
#
#     return max_word

# file = open('numbers.txt', 'r', encoding='utf-8')
# lst3 = []
# lst2 = []
# for line in file:
#     if len(line) == 4:
#         lst3.append(line)
#     if len(line) == 3:
#         lst2.append(int(line[:2]))
# print(len(lst3))
# print(sum(lst2))


# def find_lines_len_more_6(file_name:str) -> int:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         x = [i for i in file.read().splitlines()]
#         count = 0
#         for row in x:
#             if len(row) > 6:
#                 count += 1
#         return count


# def unique_word(file_name: str) -> int:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lst = []
#         x = [i for i in file.read().lower().split()]
#         print(x)
#         for word in x:
#             if word.lower() not in lst:
#                 lst.append(word)
#         return len(set(lst))
#
#
# print(unique_word('lorem.txt'))


# def word_dict(file_name: str) -> dict:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         words = {}
#         x = [i for i in file.read().lower().split()]
#         # print(x)
#         for word in x:
#             words.setdefault(word.upper(), 0)
#             words[word.upper()] += 1
#         return f'words={words}'
#
#
# print(word_dict('lorem.txt'))


# def long_words(file_name: str) -> list:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         words = {}
#         lst = []
#         x = [i for i in file.read().upper().split()]
#         for i in x:
#             if i in words:
#                 words[i] = words[i] + 1
#             else:
#                 words[i] = 1
#         for key in words:
#             if key.endswith('ЕЯ') == True:
#                 lst.append(key)
#         lst.sort(key=lambda item: (len(item), item))
#         print(*lst, sep="\n")
#
#
# long_words('words.txt')
