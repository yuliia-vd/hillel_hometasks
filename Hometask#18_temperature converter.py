# Написать приложение, которое оперирует с объектом типа температура
# Объект "температура" при создании должен
# принимать температуру
# иметь возможность возвращать заданную температуру в разных шкалах
# поддерживать сложение, вычитание и операции сравнения

class Temperature:

    def __init__(self, temp_in, measure):
        self.f = Temperature.to_f(temp_in, measure)
        self.k = Temperature.to_k(temp_in, measure)
        self.c = Temperature.to_c(temp_in, measure)

    @staticmethod
    def to_f(temp_in, measure):
        if measure == 'f':
            temp_f = temp_in
        elif measure == 'k':
            temp_f = 1.8*(temp_in-273.15)+32
        elif measure == 'c':
            temp_f = temp_in*1.8 + 32
        return temp_f

    @staticmethod
    def to_k(temp_in, measure):
        if measure == 'k':
            temp_k = temp_in
        elif measure == 'f':
            temp_k = (temp_in-32)/1.8 +273.15
        elif measure == 'c':
            temp_k = temp_in + 273.15
        return temp_k

    @staticmethod
    def to_c(temp_in, measure):
        if measure == 'c':
            temp_c = temp_in
        elif measure == 'f':
            temp_c = (temp_in-32)/1.8
        elif measure == 'k':
            temp_c = temp_in - 273.15
        return temp_c

    def __eq__(self, other):
        if self.c == other.c:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.c > other.c:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.c >= other.c:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.c < other.c:
            return True
        else:
            return False

    def __le__(self, other):
        if self.c <= other.c:
            return True
        else:
            return False

    def __cmp__(self, other):
        if self.c == other.c:
            return 0
        elif self.c > other.c:
            return 1
        else:
            return -1

    def __add__(self, other):
        return Temperature(self.c+other.c, 'c')

    def __sub__(self, other):
        return Temperature(self.c-other.c, 'c')

    def __str__(self):
        return f'{self.f} fahrehgeit or {self.k} kelvin or {self.c} celsius'

# Проверка конвертера
print('Перевод в Фаренгейты')
print(Temperature.to_f(30, 'c'))
print(Temperature.to_f(30, 'k'))
print(Temperature.to_f(30, 'f'))
print('Перевод в Кельвины')
print(Temperature.to_k(30, 'f'))
print(Temperature.to_k(30, 'c'))
print(Temperature.to_k(30, 'k'))
print('Перевод в Цельсии')
print(Temperature.to_c(30, 'k'))
print(Temperature.to_c(30, 'f'))
print(Temperature.to_c(30, 'c'))
print('------------------------')

print('Перевод из Кельвинов')
temp1 = Temperature(30, 'k')
print(f'{temp1.c} c')
print(f'{temp1.f} f')
print(f'{temp1.k} k')

print('Перевод из Фаренгейтов')
temp2 = Temperature(30, 'f')
print(f'{temp2.c} c')
print(f'{temp2.k} k')
print(f'{temp2.f} f')

print('Перевод из Цельсиев')
temp3 = Temperature(30, 'c')
print(f'{temp3.k} k')
print(f'{temp3.f} f')
print(f'{temp3.c} c')


# операции сравнения
print('Операции сравнения:')
temp4 = Temperature(30, 'k')
temp5 = Temperature(35, 'k')
print(temp4.c == temp5.c)
print(Temperature.__eq__(temp4,temp5))
print(Temperature.__gt__(temp4,temp5))
print(Temperature.__ge__(temp4,temp5))
print(Temperature.__lt__(temp4,temp5))
print(Temperature.__le__(temp4,temp5))
print(Temperature.__cmp__(temp4,temp5))
print('*****************************')
print(temp4 > temp5)
print(temp4 >= temp5)
print(temp4 < temp5)
print(temp4 <= temp5)
print(temp4 == temp5)
print(temp4 != temp5)

# операции сложения и вычитания, метод str
print('Операции cложения и вычитания:')
print((temp4 + temp5).c)
print((temp4 - temp5).c)

print('Метод str:')
print(Temperature.__str__(temp4))
print(temp4)
print(temp5)
