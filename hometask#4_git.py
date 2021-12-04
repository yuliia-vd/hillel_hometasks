a = 0

for number in range(1000000):

    digit1 = number // 100000
    digit2 = (number // 10000) - (number // 100000)*10
    digit3 = (number // 1000) - (number // 10000)*10
    digit4 = (number // 100) - (number // 1000)*10
    digit5 = (number // 10) - (number // 100)*10
    digit6 = number % 10

    if (digit1 + digit2 + digit3) == (digit4 + digit5 + digit6):
        a = a+1

print('Number of lucky tickets is', a)