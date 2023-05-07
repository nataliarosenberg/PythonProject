 # Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”, a następnie:

quote = "Honesty is the first chapter in the book of wisdom."
#Policz wszystkie znaki w napisie:
length_word = int(len(quote))
print(length_word)

# Nie modyfikując zmiennej wyświetl słowo wisdom:
tablica_quote=quote.split(" ")
len_tab=len(tablica_quote)
word=tablica_quote[9]
len_word=len(word)
print(word[:len_word-1])

#Wyświetl tylko pierwszą połowę tekstu

half=tablica_quote[:len_tab//2]
print(' '.join(half))

#Wyświetl tylko kropkę
print(quote[length_word-1])

#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[length_word//2::3])

#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])

#Wyświetl cały cytat odwrotnie
print(quote[::-1])

#Zamień wisdom na słowo friendship
print(quote.replace("wisdom","friendship"))


