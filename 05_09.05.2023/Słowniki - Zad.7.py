"""
Usuń duplikat z podanej list i utwórz na jej bazie krotkę.
Znajdź minimalną i maksymalną liczbę w krotce.
"""

list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

list_to_set = set(list)
print(list_to_set)

for i in list_to_set :
    count= list.count(i)
    if count >1 :
       print(i)
max = max(list_to_set)
min = min(list_to_set)
print(max, min)

"""
2 opcja: 
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
example_set = set(example_list)
print(example_set)
example_tuple = tuple(example_set)
print(example_tuple)
print(min(example_tuple))
print(max(example_tuple))"""