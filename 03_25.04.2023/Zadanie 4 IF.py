"""
Utwórz zmienną przechowującą dowolny ciąg znaków.
Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
"""
word = input(" Please enter word: ")
word_length = len(word)
print(word_length)
include_a=word.count("a")
print(include_a)
if word_length >= 5 and include_a > 0:
    print(word.replace("a","z"))
else:
    print(word)