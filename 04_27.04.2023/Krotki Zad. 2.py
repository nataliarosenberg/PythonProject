""" Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je."""


Tuples = ("34", "17", "25", "41", "12", "194", "41", "3", "12", "17")
tuples_to_set = set(Tuples)
print(tuples_to_set)

for i in tuples_to_set :
    count= Tuples.count(i)
    if count >1 :
       print(i)

