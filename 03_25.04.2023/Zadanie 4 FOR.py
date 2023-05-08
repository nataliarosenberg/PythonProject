"""
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8).
"""
N = int(input("Enter number > 1 <= 8 --> "))

if N <= 8 and N > 0:
    silnia = 1
    for i in range(1, N+1):
        silnia = silnia*i
    print("Silnia z ", i, "wynosi", silnia)
else:
    print("I can't calculate because your number is greater than 8")