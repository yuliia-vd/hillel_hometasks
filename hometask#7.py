# Пусть пользователь вводит строку, искомое слово и слово-замену
# Заменить в строке искомое слово на слово-замену
# вывести колличество замен

str_1 = input("Введите строку ")
str_2 = input("Введите искомое слово ")
str_3 = input("Введите слово-замену ")

print(str_1.replace(str_2, str_3))

print(str_1.count(str_2))
