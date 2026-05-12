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

def update_user(users_data: list) ->None:
    name=input('Podaj imię użytkownika do zmiany: ')

    for user in users_data:
        if user['username'] == name:
            user['username']=input('Podaj nowe imie')
            user['location']=input('Podaj nową loklaizację: ')
            user['posts']=input('Podaj liczbę postów: ')
    users_data(user)
    print(user)

def get_coordinates(location:str)->list:


    url=f'https://pl.wikipedia.org/wiki/{location}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)

    response_html=BeautifulSoup(response.text, 'html.parser')
    response_html_latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    response_html_longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    return[response_html_latitude,response_html_longitude]

for user in users:
    print(get_coordinates(location=user['location']))