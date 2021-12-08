num1 = int(input("num1 "))
action = input("action ")

while action != "=":

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

print(num1)


