import datetime
import string

def print_star(func_in):
    def wrapped_func(*args, **kwargs):
        print('***************************************')
        result = func_in(*args, **kwargs)
        print('----------------------------------------')
        return result
    return wrapped_func

def calc_time(func_in):
    def wrapped_func(*args, **kwargs):
        start_time = datetime.datetime.now()
        val_in_func = func_in(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(end_time - start_time)
        return val_in_func
    return wrapped_func

@print_star
@calc_time
def cesar(text, shift):
    alphabet = string.ascii_letters
    new_text = ''
    for itm in text:
        if itm in alphabet:
            char_index = alphabet.index(itm)
            new_index = (char_index + shift) % len(alphabet)
            new_index
            new_text = new_text + alphabet[new_index]
        else:
            new_text = new_text +itm

    return new_text

@print_star
@calc_time
def undo_cesar(text, shift):
    alphabet = string.printable
    new_text = ''
    for itm in text:
        if itm in alphabet:
            char_index = alphabet.index(itm)
            new_index = (char_index - shift) % len(alphabet)
            new_text = new_text + alphabet[new_index]
        else:
            new_text = new_text +itm

    return new_text

@print_star
@calc_time
def lucky_tikets():
    a = 0
    for ticket_number in range(1000000):
        ticket_number = str(ticket_number)
        ticket_number = ticket_number.rjust(6, '0')
        left_side = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
        right_side = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
        if left_side == right_side:
            a = a + 1

    # print('Number of lucky tickets №1 is', a)

text_to = 'The, quick brown fox jumps. over the lazy# dog46'
val1 = cesar(text_to,5)
val2 = undo_cesar(val1,5)
val3 = lucky_tikets()