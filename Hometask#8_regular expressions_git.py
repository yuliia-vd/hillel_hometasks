import re

while True:
    telephone_number = input()
    if telephone_number == 'exit':
        break
    print(bool(re.match(r'(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)',telephone_number)))
