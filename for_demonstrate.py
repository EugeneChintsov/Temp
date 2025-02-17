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

result = {
    'proxy': {'delete': '123.234.53.22'},
    'follow': {'delete': False},
    'timeout': {'changed': {'delete': 10, 'add': 20}},
    'host': {'unchanged': 'hexlet.io'},
    'verbose': {'add': True}
}
