from mapbook_lib.model import users
from mapbook_lib.controller import read_data, add_user

while True:
    print('0 - zakończ program')
    print('1 - wyświetl znajomych')
    print('2 - dodaj zanjomego')

    choose=input('wybierz opcje: ')
    if choose == '0':
        break
    if choose == '1':
        read_data(users[1:])
    if choose == '2':
        add_user(users[1:])