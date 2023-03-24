def change(obj):
    obj = obj.replace(',', '')
    return obj


def change1(obj):
    temp = 0
    if (obj.isnumeric() == True) & (obj != '0'):
        temp = obj
    return temp


def change2(obj):
    s = ''
    t = obj.split()[0:3]
    for i in t:
        s = s + ' ' + i
    return s