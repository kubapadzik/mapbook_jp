
users: list = [
    {'username': 'Oliwia','location':'Łódź','posty':1,'usermessage':['życzenia1', 'kocham Polonie1',"sprzedam opla2", 'kiwi3']},
    {'username': 'Paweł', 'location':'Ostróda','posty':2,'usermessage':['życzenia1', 'kocham Polonie1',"sprzedam opla2",]},
    {'username': 'Eliza', 'location':'Radom','posty':3,'usermessage':['życzenia1', 'kocham Polonie1']},
    {'username': 'Filip', 'location':'Dęblin','posty':4,'usermessage':['życzenia1', 'kocham Polonie1',"sprzedam opla2", 'kiwi3']},
]

for user in users[1:]:
    print(f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posty']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


    # Twoj znajomy filip z miejscowości Dęblin opublikował 1 post o treści: życzenia