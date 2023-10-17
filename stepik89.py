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


# from string import ascii_lowercase
# import json
#
# alphabet = {}
# for i in range(len(ascii_lowercase)):
#     alphabet[chr(97 + i)] = i + 1
# json_data = json.dumps(alphabet)
# print(json_data)


# import json
#
# maximum = 0
# max_name = ''
# max_lastname = ''
#
# with open('manager_sales.json') as file:
#     data = json.load(file)
#
#     for element in data:
#         name = element['manager']['first_name']
#         lastname = element['manager']['last_name']
#         total = 0
#         for car in element['cars']:
#             total += car['price']
#         if total > maximum:
#             maximum = total
#             max_name = name
#             max_lastname = lastname
# print(max_name, max_lastname, maximum)


# import json
#
# maximum = 0
# max_group = None
# with open('group_people.json', 'r') as file:
#     data = json.load(file)
#
#     for group in data:
#         id_group = group['id_group']
#         count_female = 0
#         for person in group['people']:
#             if person['gender'] == 'Female' and person['year'] > 1977:
#                 count_female += 1
#         if count_female > maximum:
#             maximum = count_female
#             max_group = id_group
# print(max_group, maximum)


# import json
#
# with open('Abracadabra__1_.txt', 'r') as file, open('Alphabet.json', 'r') as decod_keys:
#     data = json.load(decod_keys)
#     x = [i for i in file.read()]
#     new_str = ''
#     for letter in x:
#         if letter in data:
#             new_str += data[letter]
#         else:
#             new_str += letter
#     print(new_str)


# import json
#
# people = ('[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, '
#           '{"name": "Matthew King", "country": "Colombia", "age": 34}, {"name": "Sean Sullivan", "country": '
#           '"Mayotte", "age": 40}, {"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, '
#           '{"name": "Sarah Contreras", "country": "Honduras", "age": 82}, {"name": "Danielle Williams", "country": '
#           '"Togo", "age": 91}, {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}, {"name": "Patricia '
#           'Wilkerson", "country": "Georgia", "age": 22}, {"name": "Zachary Scott", "country": "Brunei Darussalam", '
#           '"age": 55}, {"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23}, {"name": "Christina Fernandez", '
#           '"country": "Burundi", "age": 71}, {"name": "Allen Norton", "country": "Montserrat", "age": 79}, '
#           '{"name": "Scott Arroyo", "country": "Montenegro", "age": 72}, {"name": "Brooke Boyd", "country": "Latvia", '
#           '"age": 74}, {"name": "Jerry Morrow", "country": "San Marino", "age": 23}, {"name": "Danielle Bradshaw", '
#           '"country": "Vietnam", "age": 64}, {"name": "Jerry Thompson", "country": "Belgium", "age": 30}, '
#           '{"name": "Mark Jordan", "country": "Comoros", "age": 89}, {"name": "Joseph Berger", "country": "Cook '
#           'Islands", "age": 94}, {"name": "Gina Brooks", "country": "Samoa", "age": 51}, {"name": "Walter Duran", '
#           '"country": "Chad", "age": 67}, {"name": "John Martinez", "country": "Wallis and Futuna", "age": 65}, '
#           '{"name": "Johnny Glover", "country": "Eritrea", "age": 72}, {"name": "Lindsay Moore", "country": '
#           '"Liberia", "age": 53}, {"name": "Kimberly Burton", "country": "Nicaragua", "age": 92}, '
#           '{"name": "Jacqueline Ballard", "country": "Nigeria", "age": 78}, {"name": "Charles Thompson", "country": '
#           '"Saudi Arabia", "age": 50}, {"name": "Suzanne Roberts", "country": "Serbia", "age": 43}, {"name": "David '
#           'Decker", "country": "South Africa", "age": 71}, {"name": "Christopher Perez", "country": "Cayman Islands", '
#           '"age": 49}, {"name": "Debra Hall", "country": "Greece", "age": 13}, {"name": "John King", "country": '
#           '"Bahamas", "age": 40}, {"name": "Justin Galvan", "country": "Namibia", "age": 19}, {"name": "Jacqueline '
#           'Berger", "country": "Yemen", "age": 59}, {"name": "Shawn Robinson", "country": "Saint Pierre and '
#           'Miquelon", "age": 32}, {"name": "Kristen Garcia", "country": "Portugal", "age": 48}, {"name": "Christopher '
#           'Barry", "country": "French Polynesia", "age": 23}, {"name": "Alejandra Cook", "country": "Egypt", '
#           '"age": 16}, {"name": "Jill Harrell", "country": "Comoros", "age": 49}, {"name": "Sara Zimmerman", '
#           '"country": "Brazil", "age": 26}, {"name": "Mrs. Charlene Flores", "country": "New Caledonia", "age": 75}, '
#           '{"name": "Melissa Crawford", "country": "Lebanon", "age": 17}, {"name": "Larry Wong", "country": "New '
#           'Caledonia", "age": 6}, {"name": "Brenda Acosta", "country": "Grenada", "age": 48}, {"name": "Latoya '
#           'Terry", "country": "Saint Martin", "age": 41}, {"name": "Seth Luna", "country": "Sao Tome and Principe", '
#           '"age": 59}, {"name": "Micheal Adams", "country": "Barbados", "age": 53}, {"name": "Susan Carroll", '
#           '"country": "Somalia", "age": 64}, {"name": "Douglas Morris", "country": "Thailand", "age": 24}, '
#           '{"name": "Dennis Wagner", "country": "Zimbabwe", "age": 66}, {"name": "Kristin Johnson", "country": '
#           '"Niue", "age": 71}, {"name": "Steven Krause", "country": "Turkmenistan", "age": 84}, {"name": "Jared '
#           'Smith", "country": "Colombia", "age": 46}, {"name": "Lauren Anderson", "country": "Christmas Island", '
#           '"age": 46}, {"name": "Joshua Spencer", "country": "Russian Federation", "age": 38}, {"name": "Maria '
#           'Edwards", "country": "Hungary", "age": 78}, {"name": "Anne Lee", "country": "United States of America", '
#           '"age": 10}, {"name": "James Mckenzie", "country": "Uganda", "age": 43}, {"name": "Joshua Gallegos", '
#           '"country": "United States Minor Outlying Islands", "age": 27}, {"name": "Paul Herrera", "country": '
#           '"Kiribati", "age": 17}, {"name": "Veronica White", "country": "Gabon", "age": 88}, {"name": "Michael '
#           'Hall", "country": "China", "age": 43}, {"name": "Sabrina Thompson", "country": "Chad", "age": 27}, '
#           '{"name": "Jennifer Archer", "country": "Korea", "age": 45}, {"name": "Christina Simmons", "country": '
#           '"Israel", "age": 80}, {"name": "Travis White", "country": "Central African Republic", "age": 31}, '
#           '{"name": "Dennis Hernandez", "country": "Slovenia", "age": 66}, {"name": "Matthew Richards", "country": '
#           '"Svalbard & Jan Mayen Islands", "age": 34}, {"name": "Stephen Curry", "country": "Finland", "age": 92}, '
#           '{"name": "Margaret Williamson", "country": "Hong Kong", "age": 86}, {"name": "Mary Estes", "country": '
#           '"Montenegro", "age": 19}, {"name": "Alex Scott", "country": "Christmas Island", "age": 67}, {"name": "John '
#           'Andrews", "country": "Bahamas", "age": 68}, {"name": "Jonathan Willis", "country": "Saint Martin", '
#           '"age": 23}, {"name": "Olivia Campos", "country": "Armenia", "age": 72}, {"name": "Diana Davis", '
#           '"country": "Azerbaijan", "age": 54}, {"name": "Jack Cummings", "country": "Martinique", "age": 94}, '
#           '{"name": "Kaitlyn Mcdonald", "country": "Austria", "age": 12}, {"name": "Maria Blake", "country": '
#           '"Pitcairn Islands", "age": 91}, {"name": "Kelly Thomas", "country": "Ethiopia", "age": 74}, {"name": "John '
#           'Terrell Jr.", "country": "India", "age": 50}, {"name": "Lindsay Wood", "country": "United Arab Emirates", '
#           '"age": 72}, {"name": "Matthew Gilbert", "country": "Madagascar", "age": 86}, {"name": "Tanner Johnson", '
#           '"country": "Congo", "age": 11}, {"name": "Michael Garcia", "country": "Liberia", "age": 45}, '
#           '{"name": "Nicole Johnson", "country": "Barbados", "age": 54}, {"name": "William Lee", "country": '
#           '"Lithuania", "age": 59}, {"name": "Jeffrey Coffey", "country": "Faroe Islands", "age": 88}, '
#           '{"name": "Sandra Freeman", "country": "Philippines", "age": 35}, {"name": "Latoya Maxwell", "country": '
#           '"Sweden", "age": 12}, {"name": "Darius Blevins", "country": "Thailand", "age": 29}, {"name": "Teresa '
#           'Newman", "country": "Jersey", "age": 6}, {"name": "Larry Bray", "country": "Brunei Darussalam", '
#           '"age": 21}, {"name": "Adam Roberson", "country": "Jordan", "age": 71}, {"name": "Michael Gomez", '
#           '"country": "Tajikistan", "age": 37}, {"name": "Abigail Mccarthy", "country": "Kiribati", "age": 85}, '
#           '{"name": "Tom Morris", "country": "Cayman Islands", "age": 27}, {"name": "Kevin Wagner", "country": '
#           '"Suriname", "age": 55}, {"name": "Peggy Bryant", "country": "Korea", "age": 36}, {"name": "Erik '
#           'Mclaughlin", "country": "Austria", "age": 24}]')
# data = json.loads(people)
# data = sorted(data, key=lambda x: (x['age'], x['name']))
# for i in data:
#     print(f"{i['name']}, {i['country']}, {i['age']}")


# import json
#
# json_string = '''
# {
#     "customers": [
#         {
#             "userid": 123456,
#             "username": "Allie Hsu",
#             "phone": [
#                 "000-001-0002",
#                 "000-002-0002"
#             ],
#             "is_vip": true
#         },
#         {
#             "userid": 223678,
#             "username": "Donald Duck",
#             "phone": null,
#             "is_vip": false
#         }
#     ]
# }
# '''
#
# data = json.loads(json_string)
# print(data['customers'][0]['username'])
