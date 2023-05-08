""""
 Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set."""

Tuple_1 = ("Pasta", "Kubek", "Szczotka", "Mydło")
Tuple_2 = ("Recznik", "Papier", "Piżama", "22")

List_1 = Tuple_1[0::2]
List_2 = Tuple_2[1::2]
print(List_1)
print(List_2)
MyList = List_1 + List_2
list_to_set= set(MyList)
print(list_to_set)

