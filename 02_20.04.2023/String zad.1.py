"""Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu."""

word = "automatyzacja"
mid_index = len(word) // 2
mid_chars = word[mid_index - 1 : mid_index + 2]
print(mid_chars)