def get_diff(data1, data2):

    keys = data1.keys() | data2.keys()
    result = {}
    
    for key in keys:
            # Доделать:
            # Сейчас nested создается отдельно и ключ отдельно , \
            # и наверное nested в словаре не нужен вообще? 

                # if (isinstance(data1.get(key, 'Nope'), dict) and isinstance(data2.get(key, 'Nope'), dict)):
                # result = {'nested':get_diff(data1[key], data2[key])}
        
        # if not (isinstance(data1[key], dict) and isinstance(data2[key], dict)):
            if key not in data1:
                result[key] = {'add':data2[key]}
            elif key not in data2:
                result[key] = {'delete':data1[key]}
            
            if key in data1 and key in data2:
                if data1[key] == data2[key]:
                    result[key] = {'unchanged':data1[key]}
            
                result[key] = {'changed': {'delete':data1[key], 'add':data2[key]}}

    return result
