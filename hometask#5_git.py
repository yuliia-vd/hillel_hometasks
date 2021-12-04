# вводим число
number = int(input('Enter your positive integer number '))

# перебираем все числа от 2 до введенного числа:
for number in range(2, number):

# проверяем, простое ли это число перебирая его все делители i
    for i in range(2, number):

        if number % i == 0:
            break

    else:
        print(number)