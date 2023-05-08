"""
Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
"""

List = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
length = len(List)
split = length //3

List_1 = List[:split]
List_2 = List[split : split*2]
List_3 = List[split*2:]

List_1.reverse()
List_2.reverse()
List_3.reverse()

print(List_1)
print(List_2)
print(List_3)