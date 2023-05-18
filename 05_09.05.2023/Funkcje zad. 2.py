"""
▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.
"""

num = float(input(" Podaj liczbę: "))

def number_check(num):
    if num % 2 == 0:
        print(num, '-Liczba jest parzysta')
        return True
    else:
        print(num,'- Liczba jest nieparzysta')
        return False

number_check(num)
