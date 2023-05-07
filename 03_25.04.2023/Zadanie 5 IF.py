"""Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę, 1 dużą literę i
mieć długość conajmniej 8 znaków.
Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
 Wyświetl różne komunikaty w zależności od rodzaju błędu."""

password =  "Hasłooooo2"

if len(password) < 8:
    print('Password too short')
if password.isalnum() and password.isalpha():
    print("Password needs at least one digit")
if password.isalnum() and password.isdigit():
    print('Password needs at least one letter')
if password.islower():
    print('Password needs at least 1 lower letter')
if password.isupper():
    print('Password needs at least one upper letter')

print(f'super [not] secure password here -> {password}')
