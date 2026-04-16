from mapbook_lib.model import users
from mapbook_lib.controller import read_data

read_data(users[1:])
while True:
    print('0 - zakończ program')
    print('1 - wyświetl znajomych')

    choose=input('wybierz opcje: ')
    if choose == '0':
        break
    if choose == '1':
        read_data(users[1:])