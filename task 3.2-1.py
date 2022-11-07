d = {}


# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key]+=[value]
    elif 2*key in d:
        d[2*key] +=[value]
    elif 2*key not in d:
        d[2 * key] = list()
        d[2 * key] += [value]


# не добавляйте кода вне функции
print(update_dictionary(d,1,-1))
print(d)
print(update_dictionary(d,2,-2))
print(d)
print(update_dictionary(d, 1, -3))
print(d)