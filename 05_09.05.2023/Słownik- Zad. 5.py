"""
W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce
Zadbaj o sposób wyświetlania np.:
"""

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

#zmienic na małe litery
# usunąc z niego przecinki
poem = poem.lower().replace(",","").split()



#tworzyć pusty słownik, w którym pojawia się
#{słowo: ile razy}

counting_word= {}

#iterować po wierszu - słowo po słowie
#jeżeli słowo występuje w słowniku to dodajemy+1 do wartośc tego słowa
# w przeciwnym wypadku musimy dodać klucz do słownika wartości 1

for word in poem:
    if word in counting_word:
        counting_word[word] += 1
    else:
        counting_word[word] = 1

print(counting_word)

for word, counter in counting_word.items():
    print("*", word, "-", counter)