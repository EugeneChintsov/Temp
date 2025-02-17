#Два плоских словаря
# и ожидаемый результат сравнения в словаре
data1 = {
    "host": "hexlet.io",
    "timeout": 10,
    "proxy": "123.234.53.22",
    "follow": False
}

data2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}
result_1_2 = {'host': {'unchanged': 'hexlet.io'}, 'timeout': {'changed': {'delete': 10, 'add': 20}}, 'verbose': {'add': True}, 'follow': {'delete': False}, 'proxy': {'delete': '123.234.53.22'}}

# тоже самое в человекочитаемом виде , для удобства:
# result_1_2 = {
#     'proxy': {'delete': '123.234.53.22'},
#     'follow': {'delete': False},
#     'timeout': {'changed': {'delete': 10, 'add': 20}},
#     'host': {'unchanged': 'hexlet.io'},
#     'verbose': {'add': True}
# }


# Два Неплоских словаря c изменением конечных значений во вложенном словаре
# и ожидаемый результат сравнения в словаре
data3 = {
    "host": "hexlet.io",
    "timeout": {
        "first": "10",
        "second": "20"
        },
    "proxy": "123.234.53.22",
    "follow": False
}

data4 = {
    "timeout": {
        "first": "30",
        "second": "40"
        },
    "verbose": True,
    "host": "hexlet.io"
}

result_3_4 = {'host': {'unchanged': 'hexlet.io'}, 'proxy': {'delete': '123.234.53.22'}, 'timeout': {'second': {'changed': {'delete': '20', 'add': '40'}}, 'first': {'changed': {'delete': '10', 'add': '30'}}}, 'verbose': {'add': True}, 'follow': {'delete': False}}

# тоже самое в человекочитаемом виде , для удобства:
# result_3_4 = {
#     'timeout': {
#         'first': {
#             'changed': {
#                 'delete': '10',
#                 'add': '30'}
#         },
#         'second': {
#             'changed': {
#                 'delete': '20',
#                 'add': '40'}
#         }
#     },
#     'host': {'unchanged': 'hexlet.io'},
#     'verbose': {'add': True},
#     'proxy': {'delete': '123.234.53.22'},
#     'follow': {'delete': False}
# }

# Два Неплоских словаря:
# c 2 уровнями вложенности словарей,
# c изменением конечных значений во вложенном словаре
# и ожидаемый результат сравнения в словаре

data5 = {
    "host": "hexlet.io",
    "timeout": {
        "first": {
            "short": 10,
            "long": 50
        },
        "second": "20"
        },
    "proxy": "123.234.53.22",
    "follow": False
}

data6 = {
    "timeout": {
        "first": {
            "short": 60,
            "long": 115
        },
        "second": "40"
        },
    "verbose": True,
    "host": "hexlet.io"
}

result_5_6 = {'proxy': {'delete': '123.234.53.22'}, 'verbose': {'add': True}, 'follow': {'delete': False}, 'host': {'unchanged': 'hexlet.io'}, 'timeout': {'first': {'long': {'changed': {'delete': 50, 'add': 115}}, 'short': {'changed': {'delete': 10, 'add': 60}}}, 'second': {'changed': {'delete': '20', 'add': '40'}}}}

# тоже самое в человекочитаемом виде , для удобства:
# result_5_6 = {
#     'proxy': {
#         'delete': '123.234.53.22'
#     },
#     'verbose': {
#         'add': True
#     },
#     'follow': {
#         'delete': False
#     },
#     'host': {
#         'unchanged': 'hexlet.io'
#     },
#     'timeout': {
#         'first': {
#             'long': {
#                 'changed': {
#                     'delete': 50,
#                     'add': 115}
#             },
#             'short': {
#                 'changed': {
#                     'delete': 10,
#                     'add': 60
#                 }
#             }
#         },
#         'second': {
#             'changed': {
#                 'delete': '20',
#                 'add': '40'
#             }
#         }
#     }
# }

# Два Неплоских словаря:
# c 2 уровнями вложенности словарей,
# c переименованием ключа , содержащего словарь 
# с конечными значениями
# и ожидаемый результат сравнения в словаре

data6 = {
    "timeout": {
        "first": {
            "short": 60,
            "long": 115
        },
        "second": "40"
        },
    "verbose": True,
    "host": "hexlet.io"
}

data7 = {
    "timeout": {
        "first": {
            "shortt": 50,
            "long": 100
        },
        "second": "40"
        },
    "verbose": True,
    "host": "hexlet.io"
}

result_6_7 = {'verbose': {'unchanged': True}, 'host': {'unchanged': 'hexlet.io'}, 'timeout': {'first': {'short': {'delete': 60}, 'long': {'changed': {'delete': 115, 'add': 100}}, 'shortt': {'add': 50}}, 'second': {'unchanged': '40'}}}

# тоже самое в человекочитаемом виде , для удобства:
# result_6_7 = {
#     'verbose': {
#         'unchanged': True
#     },
#     'host': {
#         'unchanged': 'hexlet.io'
#     },
#     'timeout': {
#         'first': {
#             'short': {
#                 'delete': 60
#             },
#             'long': {
#                 'changed': {
#                     'delete': 115,
#                     'add': 100}
#             },
#             'shortt': {
#                 'add': 50
#             }
#         },
#         'second': {
#             'unchanged': '40'
#         }
#     }
# }


