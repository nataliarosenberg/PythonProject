"""Napisz funkcję, która pyta użytkownika
o pary książka + ocena i zapisuje je w programie"""
"""
def add_books(number):

    library= {}

    for i in range(number):
        title = input("Podaj tytuł książki:")
        review = input("Jak oceniasz ksiazke od 1-10: ")
        library[title] = review
    return library

# głowna część
counter = int(input("Ile ksiazek chcesz podać"))
data = add_books(counter)
print(data)
shelf = list(data.items())
print(shelf)

# Napisz funkcje, która zapyta o numer książki
#i wyświtli tytuł z oceną.

def get_book(library):
    library = list(library.items)
    number = int(input("podaj nr ksiazki do sprawdzenia (od 1 do X): "))
    print(library[number-1])
    for i in range(number):
        title = input("Podaj tytuł książki:")
        review = input("Jak oceniasz ksiazke od 1-10: ")
        library[title] = review
    return library
counter = int(input("Podaj numer ksiązki: "))
data = add_books(counter)
print(data)
get_book(data)
"""
def add_books(number):
    library = {}

    for i in range(number):
        title = input("Podaj tytuł książki:")
        review = input("Jak oceniasz książkę od 1-10")
        library[title] = review

    return library


def get_book(library):
    library = list(library.items())
    size = len(library)

    while True:
        number = int(input(f"Podaj numer ksiazki do sprawdzenia (od 1 do {size}):"))
        if number > size or number < 1:
            print("Nie ma takiej ksiazki, sprobuj jeszcze raz")
        else:
            break

    title, review = library[number-1]
    print(f'Ksiazka pt "{title}" ma ocene {review}')


# ---- glowna czesc
counter = int(input("Ile książek chcesz dodać"))
data = add_books(counter)
print(data)
get_book(data)