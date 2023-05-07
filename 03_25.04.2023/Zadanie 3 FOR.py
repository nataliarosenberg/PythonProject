
"""Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli
sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55"""

#1 -> 1
#2 + 1 -> 3
#3+3 -> 6

a = 0
for i in range(1,11):
    a = a + i # a += i
    print(a)