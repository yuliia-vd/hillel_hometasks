# Написать функцию которая принимает два числа
# и возвращает в качестве результата
# наибольший общий делитель полученных двух чисел

def greatest_common_devisor(x,y):
    x_devisors = []
    y_devisors = []
    common_devisors = []
    for i in range(1, x+1):
        if x%i == 0:
            x_devisors.append(i)
    print(x_devisors)
    for i in range(1, y+1):
        if y%i == 0:
            y_devisors.append(i)
    print(y_devisors)
    for i in x_devisors:
        if i in y_devisors:
            common_devisors.append(i)
    print(f'greatest common dividor is {max(common_devisors)}')


greatest_common_devisor(40,50)
