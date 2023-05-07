 # Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

Title = input("Podaj tytul książki--> ")
Author = input("Podaj nazwisko  autora księżki --> ")
Pages = input("Podaj liczbe strony -->")

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

print(Title.isalpha())
print(Author.isalpha())
print(Pages.isdigit())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

print(Title.capitalize())
print(Author.capitalize())

# Połącz dane w jeden ciąg book za pomocą spacji

polacz = [Title,Author,Pages]
book=" ".join(polacz)
print(book)

# Policz liczbę wszystkich znaków w napisie book

len_book=len(book)
print("Liczba znakow w zmiennej book to ", len_book)
