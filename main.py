users: list = [
    {'username': 'Oliwia', 'location': 'Łódź', 'posty': 1,
     'usermessage': ['życzenia1', 'kocham Polonie1', "sprzedam opla2", 'kiwi3']},
    {'username': 'Paweł', 'location': 'Ostróda', 'posty': 2,
     'usermessage': ['życzenia1', 'kocham Polonie1', "sprzedam opla2", ]},
    {'username': 'Eliza', 'location': 'Radom', 'posty': 3, 'usermessage': ['życzenia1', 'kocham Polonie1']},
    {'username': 'Filip', 'location': 'Dęblin', 'posty': 4,
     'usermessage': ['życzenia1', 'kocham Polonie1', "sprzedam opla2", 'kiwi3']},
]


def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posty']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


read_data(users[1:])