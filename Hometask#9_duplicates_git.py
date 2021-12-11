string = input("Enter some elements: ")
list1 = string.split(' ')
print(list1)
for i in range(len(list1)):
    if list1.count(list1[i]) > 1:
        print(list1[i])
        break
