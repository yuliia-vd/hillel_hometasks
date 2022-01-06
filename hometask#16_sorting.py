# Написать функцию, которая сортирует список чисел от меньшего к большему.
#
# Встроенные функции сортировки НЕ использовать
#
def sorting(my_list):
    for run in range(len(my_list)-1):
        for i in range(len(my_list)-1-run):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    print(my_list)

my_list = [1,4,6,-23,13,9,51,2,3,-15,0,3]
sorting(my_list)

# my_list.sort()
# print(my_list)
#
# print(sorted(my_list))
