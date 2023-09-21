# empty = None
# empty_too = None
# print(empty is empty_too)
# print(empty is not empty_too)

# print(i_love_none := [None] * 50)

# my_tuple = 1, 2, 3, 4
# print(type(my_tuple))

# lonely = 777,
# print(lonely)

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# print(min(my_tuple), max(my_tuple))

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# print(sum(my_tuple) / len(my_tuple))

# a = (1,)1
# b = ('R',)
# c = ('A',)
# d = (2,)
# result = ((a * 3) + (b * 5) + (c * 8) + (d * 5))
# print(result)

# a = int(input())
# b = int(input())
# my_tuple = tuple(range(a, b + 1))
# print(my_tuple)

# n = int(input())
# my_list = []
# for i in range(n, n ** 2 + 1):
#     if i % 2 != 0:
#         my_list.append(i)
#     else:
#         continue
# print(tuple(my_list))

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
# print(my_tuple[44])
# print(my_tuple[-9])

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
#
# slice_5_10 = my_tuple[5:11]
# slice_from_20 = my_tuple[20:]
# slice_to_35 = my_tuple[:35]
#
# print(slice_5_10)
# print(slice_from_20)
# print(slice_to_35)

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
# my_tuple = my_tuple[::-1]
# print(my_tuple)

# my_tuple = (
# 32, 45, 32, 60, 43, 19, 39, 75, 50, 12, 53, 13, 28, 70, 68, 5, 64, 55, 30, 47, 23, 20, 17, 36, 45, 31, 46, 50, 33, 45,
# 9, 41, 12, 57, 40, 43, 47, 51, 56, 54, 40, 30, 37, 23, 43, 66, 64, 27, 44, 75, 51, 2, 19, 72, 30, 8, 29, 43, 7, 73, 34,
# 65, 54, 50, 43, 6, 50, 45, 49, 30, 39, 50, 41, 70, 38, 16, 31, 51, 72, 45, 58, 39, 50, 56, 24, 30, 9, 53, 27, 31, 68,
# 56, 26, 39, 34, 50, 10, 12, 3, 27)
# print(my_tuple.count(50))

# words_tuple = ('quaint', 'leftovers', 'thesis', 'density', 'retired', 'weak', 'tolerate',
#                'sensitivity', 'primary', 'definition', 'determine', 'bring', 'monstrous',
#                'hurl', 'timetable', 'month', 'advocate', 'provoke', 'stress', 'omission')
# for i in range(len(words_tuple)):
#     print(f'Длина слова {words_tuple[i]} = {len(words_tuple[i])}')

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# lst = list(my_tuple)
# my_list = []
# for i in range(len(lst)):
#     if lst[i] % 2 != 0:
#         my_list.append(lst[i])
#     else:
#         continue
# print(f'{sum(my_list) / len(my_list)}')

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
#
# print(sum(a := [i for i in my_tuple if i % 2 == 1]) / len(a))

# my_tuple = (
# -214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593,
# 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829,
# -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543,
# 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370,
# 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -73, 29)
# t = [i for i in my_tuple if i % 2 != 0]
# print(sum(t) / len(t))

# my_dict = dict()
# print(my_dict)

# from pprint import pprint
#
# person = {
#     "name": "Vasya",
#     "surname": "Petrov",
#     "age": 25
# }
# pprint(person)

# from pprint import pprint # для красивого вывода словаря
# person = {}
# s = 'IVANOV IVAN 19 Samara SGU 4 5 5 5 4 3 5 3'
#
# s = s.split()
# print(s)
# print('-'*15)
# person['last_name'] = s[0]
# person['first_name'] = s[1]
# person['age'] = int(s[2])
# person['city'] = s[3]
# person['university'] = s[4]
#
# print(person)
# print('-'*15)
#
# person['marks'] = []
# for i in s[5:]:
#     person['marks'].append(int(i))
#
# pprint(person)

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# print(f'{sweet["name"]}\n{sweet["calories"]}\n{sweet["id"]}')

# days = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
# print(f'{days[int(input())]}')

# from pprint import pprint # для красивого вывода словаря
#
# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# sweet["weight"] = 230
# sweet["have_topping"] = True
# sweet["name"] = "SuperCake"
# sweet["calories"] = 350
# pprint(sweet)

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# del sweet["ppu"]
# del sweet["type"]
# print(sweet)

# my_dict = {}
# for i in range(1, (int(input()) + 1)):
#     my_dict[i] = i ** 2
# print(my_dict)

# from string import ascii_lowercase
#
# alphabet = {}
# for i in range(len(ascii_lowercase)):
#     alphabet[chr(97 + i)] = i + 1
# print(alphabet)

# account = {
#   "id": 5681,
#   "uid": "45f17b56-bcad-4933-8c73-a37aaa6863b9",
#   "account_number": "6733198878",
#   "iban": "GB79PNXF20678598570754",
#   "bank_name": "AAC CAPITAL PARTNERS LIMITED",
#   "routing_number": "007398728",
#   "swift_bic": "AACCGB21"
# }
# print(len(account))

# address = {
#   "id": 7973,
#   "uid": "42f2ce1d-90ab-4345-9595-0d9f42e6c085",
#   "city": "East Monteland",
#   "street_name": "Gusikowski Land",
#   "street_address": "3230 Daugherty Centers",
#   "secondary_address": "Apt. 562",
#   "building_number": "58671",
#   "mail_box": "PO Box 5313",
#   "community": "Paradise Square",
#   "zip_code": "58611",
#   "zip": "01667",
#   "postcode": "00563",
#   "time_zone": "America/New_York",
#   "street_suffix": "Burg",
#   "city_suffix": "mouth",
#   "city_prefix": "West",
#   "state": "Wisconsin",
#   "state_abbr": "NY",
#   "country": "Mali",
#   "country_code": "MH",
#   "latitude": -56.97457993706476,
#   "longitude": -104.29509072140858,
#   "full_address": "Apt. 982 4820 Leena Rest, Lake Giannaville, MN 09265-3715"
# }
# print('zip_code' in address)
# print('longitude' in address)
# print('post_code' in address)
# print('street_name' in address)
# print('number_house' in address)

# currencies = {
#     'Argentine Peso': 118362.205708,
#     'Australian Dollar': 1586.232315,
#     'Bahraini Dinar': 423.780164,
#     'Botswana Pula': 13168.450636,
#     'Brazilian Real': 5954.781483,
#     'British Pound': 834.954104,
#     'Bruneian Dollar': 1520.451015,
#     'Bulgarian Lev': 1955.83,
#     'Canadian Dollar': 1430.54405,
#     'Chilean Peso': 898463.818465,
#     'Chinese Yuan Renminbi': 7171.445692,
#     'Colombian Peso': 4447741.922165,
#     'Croatian Kuna': 7527.744707,
#     'Czech Koruna': 24313.797041,
#     'Danish Krone': 7440.613895,
#     'Emirati Dirham': 4139.182587,
#     'Hong Kong Dollar': 8786.255952,
#     'Hungarian Forint': 355958.035747,
#     'Icelandic Krona': 143603.932438,
#     'Indian Rupee': 84241.767127,
#     'Indonesian Rupiah': 16187150.010697,
#     'Iranian Rial': 47534006.535121,
#     'Israeli Shekel': 3569.191411,
#     'Japanese Yen': 129149.364679,
#     'Kazakhstani Tenge': 489292.515538,
#     'Kuwaiti Dinar': 340.959682,
#     'Libyan Dinar': 5196.539901,
#     'Malaysian Ringgit': 4717.485104,
#     'Mauritian Rupee': 49212.933037,
#     'Mexican Peso': 23130.471272,
#     'Nepalese Rupee': 134850.008728,
#     'New Zealand Dollar': 1703.649473,
#     'Norwegian Krone': 9953.078431,
#     'Omani Rial': 433.360301,
#     'Pakistani Rupee': 198900.635421,
#     'Philippine Peso': 57574.278782,
#     'Polish Zloty': 4579.273862,
#     'Qatari Riyal': 4102.552652,
#     'Romanian New Leu': 4946.638369,
#     'Russian Ruble': 86197.012666,
#     'Saudi Arabian Riyal': 4226.530892,
#     'Singapore Dollar': 1520.451015,
#     'South African Rand': 17159.831129,
#     'South Korean Won': 1355490.097163,
#     'Sri Lankan Rupee': 228245.645722,
#     'Swedish Krona': 10439.125427,
#     'Swiss Franc': 1037.792217,
#     'Taiwan New Dollar': 31334.286611,
#     'Thai Baht': 37436.518169,
#     'Trinidadian Dollar': 7636.35428,
#     'Turkish Lira': 15078.75981,
#     'US Dollar': 1127.074905,
#     'Venezuelan Bolivar': 511082584.868731
# }
# cur = input()
# if cur in currencies:
#     print(currencies[cur])
# else:
#     print(f'Нет данных по {cur}')

# account = {
#   "id": 3136,
#   "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
#   "account_number": "0847799459",
#   "iban": "GB90XTND56373623909314",
#   "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
#   "routing_number": "126602476",
#   "swift_bic": "BCYPGB2LHGB"
# }
# keys = list(account)
# print(keys)

# d1 = {'India': 'Delhi',
#       'Canada': 'Ottawa',
#       'United States': 'Washington D. C.'}
#
# d2 = {'France': 'Paris',
#       'Malaysia': 'Kuala Lumpur'}
# capitals = d1 | d2
# print(capitals)

# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# d2.update(d1)
# print(d2)

# logins = {}
# n = int(input())
# for i in range(n):
#     login = input()
#     if login in logins:
#         print(f'{login}{logins[login]}')
#         logins[login] += 1
#     else:
#         print('OK')
#         logins[login] = 1

# countries = {
#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],
#     "Norway": ["Oslo", "Bergen", "Trondheim"],
#     "England": ["London", "Birmingham", "Manchester"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "France": ["Paris", "Marseille", "Toulouse"]
# }
#
# city = input()
# is_city = False
# for keys in countries.keys():
#     if city in countries[keys]:
#         is_city = True
#         break
# if is_city:
#     print(f'INFO: {city} is a city in {keys}')
# else:
#     print(f'ERROR: Country for {city} not found')

# user = {
#     "id": 4170,
#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
#     "password": "SyUpfo1ljm",
#     "first_name": "Teresa",
#     "last_name": "Wehner",
#     "username": "teresa.wehner",
#     "email": "teresa.wehner@email.com",
#     "gender": "Non-binary",
#     "phone_number": "+674 424.561.2776",
#     "social_insurance_number": "637316241",
#     "date_of_birth": "1993-08-17"
# }
# first option
# a = user.pop("password")
# b = user.pop("last_name")
# user_up = {"secret": a, "surname": b}
# user.update(user_up)
# print(user)
# second option
# user['secret'], user['surname'] = user.pop('password'), user.pop('last_name')

# lst = list(map(int, input().split()))
# my_dict = {lst[-2]: lst[-1]}
# for i in range(-3, -len(lst)-1, -1):
#     my_dict = {lst[i]: my_dict}
# print(my_dict)

# workers = {
#     'employer1': {'name': 'Jhon', 'salary': 7500},
#     'employer2': {'name': 'Emma', 'salary': 8000},
#     'employer3': {'name': 'Brad', 'salary': 500}
# }
# workers['employer3']['salary'] = 8500
# print(workers)

# s = input().lower()
# d = {}
# for i in s:
#      if i.isalpha():
#         d[i] = d.get(i, 0) + 1
# print(d)

# supermarket = {
#     "milk": {"quantity": 20, "price": 1.19},
#     "biscuits": {"quantity": 32, "price": 1.45},
#     "butter": {"quantity": 20, "price": 2.29},
#     "cheese": {"quantity": 15, "price": 1.90},
#     "bread": {"quantity": 15, "price": 2.59},
#     "cookies": {"quantity": 20, "price": 4.99},
#     "yogurt": {"quantity": 18, "price": 3.65},
#     "apples": {"quantity": 35, "price": 3.15},
#     "oranges": {"quantity": 40, "price": 0.99},
#     "bananas": {"quantity": 23, "price": 1.29}
# }
# lst = []
# for i in supermarket:
#     lst.append(supermarket[i]['price'] * supermarket[i]['quantity'])
# print(sum(lst))

# S1 = input()
# S2 = input()
# my_dict = {}
# for i in S1:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# my_dict2 = {}
# for i in S2:
#     if i in my_dict2:
#         my_dict2[i] += 1
#     else:
#         my_dict2[i] = 1
# if my_dict == my_dict2:
#     print('YES')
# else:
#     print('NO')

# morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',}
# for i in input().lower().split():
#     for j in i:
#         print(morze.get(j) + ' ', end = '')
#     print()

# persons= [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# data0 = {}
# data = {}
# data1 = {}
# data2 = {}
# for i in range(len(persons)):
#     data0['salary'] = persons[i][1]
#     data1['gender'] = persons[i][2]
#     data2['passport'] = persons[i][3]
#     data[persons[i][0]]=data0|data1|data2
# print(data)

# data = {
#     "my_friends": {
#         "count": 10,
#         "people": [{
#             "first_name": "Kurt",
#             "id": 621547005,
#             "last_name": "Cobain",
#             "bdate": "31.8.2005"
#         }, {
#             "first_name": "Виолетта",
#             "id": 484200150,
#             "last_name": "Кастилио",
#         }, {
#             "first_name": "Иринка",
#             "id": 21886133,
#             "last_name": "Бушуева",
#             "bdate": "28.8.1942"
#         }, {
#             "first_name": "Данил",
#             "id": 282456573,
#             "last_name": "Греков",
#             "bdate": "4.7.2002"
#         }, {
#             "first_name": "Валентин",
#             "id": 184902932,
#             "last_name": "Долматов",
#             "bdate": "25.5"
#         }, {
#             "first_name": "Евгений",
#             "id": 620469646,
#             "last_name": "Шапорин",
#             "bdate": "6.12.1982"
#         }, {
#             "first_name": "Ангелина",
#             "id": 622328862,
#             "last_name": "Краснова",
#             "bdate": "4.11.1995"
#         }, {
#             "first_name": "Иван",
#             "id": 576015198,
#             "last_name": "Вирин",
#             "bdate": "2.2.1915"
#         }, {
#             "first_name": "Паша",
#             "id": 386922406,
#             "last_name": "Воронов",
#             "bdate": "27.9"
#         }, {
#             "first_name": "Ольга",
#             "id": 622170942,
#             "last_name": "Савченкова",
#             "bdate": "20.12"
#         }]
#     }
# }
# lst = []
# for i in data['my_friends']['people']:
#     lst.append(i['first_name'])
# lst.sort()
# for j in lst:
#     print(j)
