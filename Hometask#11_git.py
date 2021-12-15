# Написать функцию, которая использует конвертор в предыдущей задаче,
# но конвертирует список длинн больше одного метра
# пример списка
#
# [(1,'sm'), (2,'ft'), (4,'in'), (0.5, 'sm')]
#
# первое значение элемента это длинна в метрах, второе - во что перевести
# в данном случае переведены должны быть первые три величины
#
# Желательно применить при решении функции map и filter

list1 = [(1,'cm'), (2,'ft'), (4,'in'), (0.5, 'cm')]
print(list1)

def filter_func(x):
    if x[0]>=1:
        return True
    else:
        return False

list2 = list(filter(filter_func, list1))
print(list2)

meters = list(map(lambda x:x[0], list2))
print(meters)

measure = list(map(lambda x:x[1], list2))
print(measure)

def conv_cm (meters):
    return meters*100
def conv_ft(meters):
    return meters * 0.305
def conv_in(meters):
    return meters * 39.3701

new_list = []
for i in range(len(measure)):
    if measure[i] == 'cm':
        new_list.append(conv_cm(meters[i]))
    elif measure[i] == 'ft':
        new_list.append(conv_ft(meters[i]))
    elif measure[i] == 'in':
        new_list.append(conv_in(meters[i]))

print(new_list)
