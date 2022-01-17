# Собрать информацию по сериалу:
# 1) общая длительность серий (_embedded/episodes/runtime)
# 2) подготовить и вывести для каждой серии текст в следующем формате:
# сезон / номер серии
# Название
# описание
# ссылка на серию

import json

file_object = open('serial.json', 'r')
json_structure = json.loads(file_object.read())

#1) общая длительность серий
total_runtime = 0
for obj in json_structure['_embedded']['episodes']:
    total_runtime = total_runtime+obj['runtime']
print(f'Общая длительность серий: {total_runtime}')

#2) информация по каждой серии
for obj in json_structure['_embedded']['episodes']:
    print(obj['season'], end='/')
    print(obj['number'])
    print(obj['summary'])
    print(obj['url'])

