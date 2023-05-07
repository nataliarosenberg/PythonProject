"""3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery,
 cyfry i znaki specjalne."""

txt = input('Podaj dowolny ciąg znaków')

lower_letter = 0
upper_letter = 0
digits = 0
other_chars = 0

for char in txt:
    if char.islower():
       upper_letter += 1
    elif char.isupper():
        lower_letter += 1
    elif char.isdigit():
        digits +=1
    else:
        other_chars +=1

print("lower letter:", lower_letter)
print("upper letter:", upper_letter)
print("digits:", digits)
print("other_chars:", other_chars)