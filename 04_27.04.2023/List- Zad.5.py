Person = [["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert","Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]]

print(Person)

 # for row in Person:
 #     #print(row[0], row[1], "-", row[2])
 #     print(" - ".join(row))


print('---------')
for row in Person:
    print()
    for id, elem in enumerate(row):
        if id ==1:
            print(elem, end=' - ')
        else:
            print(elem, end=" ")
            
#for row in Person:
#    print(row)
#   for col in row:
#        print(col)
# arr =["ala", "ma","psa", "i", "kota"]
# for id in range(5):
#     if id ==2:
#         print(arr[id], end="***")
#     else:
#         print(arr[id], end="-->")
# arr = ["ala", "ma", "kota", "i", "psa"]
#
# for value in arr: # pierwszy sposób na fora - po wartościach
#     print(value)
#
#
# for index in range(5): # drugi sposób - po indeksie / numeryczynie
#     if index == 2:
#         print(arr[index], end="***")
#     else:
#         print(arr[index], end="---> ")
#
#
# print()
# print('*******************')
# for id, word in enumerate(arr):
#     print(id, word)
#     if id == 2:
#         print(word, end="***")
#     else:
#         print(word, end="---> ")
