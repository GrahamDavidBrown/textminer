import re


def words(text):
    if not len(re.findall(r'[a-z-A-Z]+', text)):
        return
    else:
        return re.findall(r'[0-9a-z-A-Z]+', text)


def phone_number(text):
    if len(text) < 10:
        return
    phone_number = re.findall(r'[0-9]', text)
    area_code_str = ""
    area_code = phone_number[:3]
    rest_num_str = ""
    for num in area_code:
        area_code_str += num
    rest_num = phone_number[3:]
    count = 0
    for num in rest_num:
        if count == 3:
            rest_num_str += "-"
        rest_num_str += num
        count += 1
    print(area_code_str)
    print(rest_num_str)
    return {'area_code': area_code_str, 'number': rest_num_str}


def money(text):
    if len(re.findall(r'[$]', text)) != 1 or text[0] != '$':
        return
    currency = text[0:]
    dollars = re.findall(r'[0-9,]+', text)
    dollars_str = ""
    print(dollars)
    print(currency)
    for group in dollars:
        for digit in group:
            pass
    return (currency)
