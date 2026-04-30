def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posty']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')

def add_user(user_data:list)->None:

    name=input('podaj imie: ')
    location=input('podaj lokalizację: ')
    posts=int(input('Podaj liczbę postów: '))
    usermessage=['']
    user_data.append({'username': name, 'location': location, 'posty': posts,
         'usermessage': usermessage},)

def remove_user(users_data: list) -> None:
    name = input('Podaj imię użytkownika do usunięcia: ')

    for user in users_data:
        if user['username'] == name:
            users_data.remove(user)
