# рабочая версия, считает правильно если все правильно вводить без проверок на isdigit
# если вводишь неправильный action или oparator, предлагает ввести далее, пока не введешь нужный оператор
num1 = int(input("num1 "))
action = input("action ")

# while (action != "exit") or (action != "=") or (num1 != "exit") or (num2 != "exit") :
while action != "=":
    # if num1.isdigit() and num2.isdigit():
    #     num1 = int(num1)
    #     num2 = int(num2)
    # else:
    #     print('Error1')

    if action in ['+', '-', '*', '/']:
        num2 = int(input("num2 "))
        if action == "+":
            num1 = num1 + num2

        elif action == "-":
            num1 = num1 - num2

        elif action == "*":
            num1 = num1 * num2

        elif action == "/":
            num1 = num1 / num2

    action = input("operator ")

    # if action == '=':
    #     print(num1)
    # break

# if action == "=":
#         print(num1)

      # if action not in ['+', '-', '*', '/']:
    #     print('Error2')

# print(Error2)
print(num1)


