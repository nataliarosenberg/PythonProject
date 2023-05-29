"""
Stwórz moduł, który zajmuje się jedynie otwieraniem plików -
oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje
oraz czy jest niepusty.
Funkcja zapisująca do pliku chroni przed nadpisaniem
istniejącego pliku.
"""
import os

def open_file(filename):
    if not os.path.exists(filename):
        print("Plik nie istnieje")
    elif os.stat(filename).st_size==0:
        print('plik jest pusty')
    else:
        with open(filename, 'r', encoding ='UTF-8') as f:
            file = f.read()
        return file

def write_file(filename, content):
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        print("plik juz istnieje i nie jest pusty")
    else:
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(content)
        print(f'plik {filename} został zapisany')