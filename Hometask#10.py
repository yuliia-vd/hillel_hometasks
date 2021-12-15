def meters_converter(meters, lenth_type = 'cm'):

    if lenth_type == 'cm':
        result = f'{meters*100} cm'
    elif lenth_type == 'feet':
        result = f'{meters*0.305} feet'
    elif lenth_type == 'inches':
        result = f'{meters*39.3701} inches'
    elif lenth_type == 'sazhen':
        result = f'{meters*2.13} sazhen'
    return result

print(meters_converter(100,'cm'))