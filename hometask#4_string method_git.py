#1 Вариант методом .rjust(6,'0')
a = 0

for ticket_number in range (1000000):
    ticket_number = str(ticket_number)
    ticket_number = ticket_number.rjust(6,'0')
    left_side = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    right_side = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
    if left_side == right_side:
        a = a + 1

print('Number of lucky tickets №1 is', a)



#2 Вариант с помощью len(ticket_number) и конкатенации нулей

a = 0

for ticket_number in range (1000000):
    ticket_number = str(ticket_number)

    if len(ticket_number) == 1:
        ticket_number = '00000' + ticket_number

    elif len(ticket_number) == 2:
        ticket_number = '0000' + ticket_number

    elif len(ticket_number) == 3 :
        ticket_number = '000' + ticket_number

    elif len(ticket_number) == 4:
        ticket_number = '00' + ticket_number

    elif len(ticket_number) == 5 :
        ticket_number = '0' + ticket_number

    left_side = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
    right_side = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

    if left_side == right_side:
        a = a + 1

print('Number of lucky tickets №2 is', a)

