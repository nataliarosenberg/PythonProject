"""
 Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.
"""
import random

start = int(input("Enter first number of the range --> "))
end = int(input("Enter last number of range -> "))

random_number = random.randint(0,100)
print(random_number)

def is_in_user(start, end, random_number):
    if random_number  in range(start, end):
        print( f"Number {random_number} is in  range ({start}, {end+1}) ")
    else:
        print(  f"Number {random_number} is not in range ({start}, {end+1})")

is_in_user(start, end,random_number)