"""
Utwórz listę lists_to_dict zawierającą listy 2 elementowe.
Przekształć ją w słownik dict_from_list.
"""
lists_to_dict = [['lion',1], ['giraffe', 2], ['elephant',3]]
dict_to_list = dict(lists_to_dict)
print(dict_to_list)
for k, v in dict_to_list.items():
    print(k,'-->', v)