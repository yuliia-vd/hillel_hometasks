import datetime

def decorator_logger(function_to_decorate):
    def wrap (*args, **kwargs):
        print(*args, **kwargs)
        start_time = datetime.datetime.now()
        result = function_to_decorate(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(end_time-start_time)
        return result
    return wrap
@decorator_logger
def lucky_tickets(*args, **kwargs):
    a = 0
    for ticket_number in range(1000000):
        ticket_number = str(ticket_number)
        ticket_number = ticket_number.rjust(6, '0')
        left_side = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
        right_side = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
        if left_side == right_side:
            a = a + 1

    print('Number of lucky tickets is', a)
@decorator_logger
def a1(*args, **kwargs):
    print(*args, **kwargs)

lucky_tickets(1, 2)
a1(159, 'abc')