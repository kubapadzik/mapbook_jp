users: list = [
    {'username': 'Oliwia', 'location': 'Łódź', 'posty': 1,
     'usermessage': ['życzenia1', 'kocham Polonie1', "sprzedam opla2", 'kiwi3']},
    {'username': 'Paweł', 'location': 'Ostróda', 'posty': 2,
     'usermessage': ['życzenia1', 'kocham Polonie1', "sprzedam opla2", ]},
    {'username': 'Eliza', 'location': 'Radom', 'posty': 3, 'usermessage': ['życzenia1', 'kocham Polonie1']},
    {'username': 'Filip', 'location': 'Dęblin', 'posty': 4,
     'usermessage': ['życzenia1', 'kocham Polonie1', "sprzedam opla2", 'kiwi3']},
]

def add_user(user_data:list)->None:

    print(users)
    name=input('podaj imie: ')
    location=input('podaj lokalizację: ')
    posts=int(input('Podaj liczbę postów: '))
    usermessage=[]
    users.append({'username': name, 'location': location, 'posty': posts,
         'usermessage': usermessage},)
    print(users)

add_user(users)
print(users)

