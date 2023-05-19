""""
▹ Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem.
 Nowa lista powinna zawierać 100 elementów."""

names_dict= { "Poland": ["Anna", "Katarzyna", "Maria","Magdalena", "Krystyna", "Monika","Malgorzata","Agnieszka","Ela","Julia"],
    "Italy": ["Sophie","Giulia","Cristina","Alice","Matilde","Emma","Giorgia","Angela","Beatrice","Domenica"],
    "France": ["Emma""Jade","Louise","Alice","Chloe","Lina","Léa","Rose","Anna","Mila"],
    "Spain": ["Martina","Julia", "Laia", "Lucia" "Maria", "Emma","Noa","Paula","Ona","Aina"],
    "Holland":["Sophie","Julia","Lieke","Emma","Sanne","Anna","Lotte","Eva","Mia","Lisa"],
    "Ireland": ["Emily","Sophie","Emma","Grace","Lily","Sarah","Lucy","Ava","Chloe","Katie"],
    "Norway": ["Emma","Nora","Olivia","Sara","Emilie","Lea","Sophie","Ella","Amaile","Mia"],
    "Scotland":["Olivia","Emily","Isla","Sophie","Amelia","Jessica","Ava","Ella","Charlotte","Aria"],
    "Switzerland":["Emma","Mia","Sophie","Lina","Lena","Lea","Lara","Emily","Nina","Anna"],
    "Sweden": ["Alice","Vera","Lilly","Ella","Wilma","Ebba","Olivia","Astrid","Alma","Elsa"]}

lista = list(names_dict.values())

list_names = []
counting_name = []

for row in lista:
    for elem in row:
        list_names.append(elem)
print(list_names)

for name in list_names:
    if (list_names.count(name)>3 ) and (counting_name.count(name) == 0):
        counting_name.append(name)
print(counting_name)

