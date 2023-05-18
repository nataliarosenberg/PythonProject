"""
Napisać funkcję, która wypisze wszystkie parzyste z przekazanej
listy elementów (wykorzystać funkcje z pkt 2)
"""
num = input("Podaj kilka liczb: ")
elements = num.split()


def number_check(num):
    if num % 2 == 0:
        return True
    else:
        return False
def num_s_check(elements):
    for e in elements:
        if number_check(int(e)):print(e)

num_s_check(elements)
