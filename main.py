from tkinter import *
import tkintermapview
import requests
from bs4 import BeautifulSoup

users:list=[]

class User:
    def __init__(self, imie: str, nazwisko: str, posty: int, lokalizacja: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posty = posty
        self.lokalizacja = lokalizacja
        self.coordinates = User.get_coordinates(self)

        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=self.imie)

    def get_coordinates(self) -> list:
        url = f'https://pl.wikipedia.org/wiki/{self.lokalizacja}'
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(url, headers=headers)

        response_html = BeautifulSoup(response.text, 'html.parser')
        response_html_latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        response_html_longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        return [response_html_latitude, response_html_longitude]

def show_users()-> None:
    listbox_lista_obiektow.delete(0, END) #czyszczenie
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, user.imie)


def remove_user()-> None:
    i = listbox_lista_obiektow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    show_users()


def show_user_details():
    i = listbox_lista_obiektow.index(ACTIVE) #edycja kliknietego uzytkownika
    imie = users[i].imie
    nazwisko = users[i].nazwisko
    posty = users[i].posty
    lokalizacja = users[i].lokalizacja


    label_imie_szczegoly_obiektu_wartosc.configure(text=imie)
    label_nazwisko_szczegoly_obiektu_wartosc.configure(text=nazwisko)
    label_liczba_postow_szczegly_obiektu_wartosc.configure(text=posty)
    label_lokalizacja_szczegoly_obiektu_wartosc.configure(text=lokalizacja)
    map_widget.set_position(users[i].coordinates[0], users[i].coordinates[1])
    map_widget.set_zoom(12)

def edit_user():
    i = listbox_lista_obiektow.index(ACTIVE)
    imie = users[i].imie
    nazwisko = users[i].nazwisko
    posty = users[i].posty
    lokalizacja = users[i].lokalizacja

    entry_imie.insert(0, imie)
    entry_nazwisko.insert(0, nazwisko)
    entry_liczba_postow.insert(0, posty)
    entry_lokalizacja.insert(0, lokalizacja)

    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda: update_user(i))

def update_user(i):
    users[i].imie = entry_imie.get()  #get to wyciaganie info
    users[i].nazwisko = entry_nazwisko.get()
    users[i].posty = entry_liczba_postow.get()
    users[i].lokalizacja = entry_lokalizacja.get()
    users[i].coordinates = User.get_coordinates(users[i])
    users[i].marker.delete(0, END)
    users[i].marker = map_widget.set_marker(users[i].coordinates[0], users[i].coordinates[1], text = users[i].imie)

    button_dodaj_uzytkownika.config(text="Dodaj użytkownika", command=add_user)
    show_users()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)

def add_user():
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    posts = entry_liczba_postow.get()
    lokalizacja = entry_lokalizacja.get()

    # print(name, surname, posts, lokalizacja)
    new_user = User(imie=name, nazwisko=surname, posty=int(posts), lokalizacja=lokalizacja)
    users.append(new_user)
    # print(users)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_lokalizacja.delete(0, END)


    entry_imie.focus() #kursor przeskakuje po enterze
    show_users()




root = Tk()

root.title("Mapbook_JP")
root.geometry("1024x760")


# FRAME
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2, padx=50, pady=20)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# RAMKA LISTA OBIKETÓW

label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista użytkowników: ")
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)


button_pokaz_szczegoly_obiektu = Button(ramka_lista_obiektow, text="Pokaż szczegoly", command=show_user_details)
button_usun_obiekt = Button(ramka_lista_obiektow, text="Usuń", command=remove_user)
button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj", command=edit_user)

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly_obiektu.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)


# RAMKA FORMULARZ

label_formularz = Label(ramka_formularz, text="Formularz: ")
label_imie = Label(ramka_formularz, text="Imię: ")
label_nazwisko = Label(ramka_formularz, text="Nazwisko: ")
label_liczba_postow = Label(ramka_formularz, text="Liczba postow: ")
label_lokalizacja = Label(ramka_formularz, text="Lokalizacja: ")


label_formularz.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_liczba_postow.grid(row=3, column=0, sticky=W)
label_lokalizacja.grid(row=4, column=0, sticky=W)


entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_liczba_postow = Entry(ramka_formularz)
entry_lokalizacja = Entry(ramka_formularz)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_liczba_postow.grid(row=3, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz, text = "Dodaj użytkownika",command = add_user)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# SZCZEGÓŁY OBIEKTU

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Szczegóły użytkownika: ")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Imię: ")
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Nazwisko: ")
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")
label_liczba_postow_szczegly_obiektu = Label(ramka_szczegoly_obiektu, text = "Liczba postow: ")
label_liczba_postow_szczegly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Lokalizacja: ")
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = "...")

label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)
label_imie_szczegoly_obiektu.grid(row=1, column=0, sticky=W)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1, sticky=W)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2, sticky=W)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3, sticky=W)
label_liczba_postow_szczegly_obiektu.grid(row=1, column=4, sticky=W)
label_liczba_postow_szczegly_obiektu_wartosc.grid(row=1, column=5, sticky=W)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6, sticky=W)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7, sticky=W)


# RAMKA MAPA
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=600, corner_radius=4)
map_widget.set_zoom(6)
map_widget.set_position(52.2, 21.0)

map_widget.grid(row=0, column=0)



root.mainloop()