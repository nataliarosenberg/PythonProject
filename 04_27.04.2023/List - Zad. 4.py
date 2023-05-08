"""
Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
"""
elements = input("Enter even number of items -->  ")
list_elements = elements.split()
length = len(list_elements)
print(length)
if length % 2 == 0:
    mid1 = list_elements[length//2-1]
    mid2 = list_elements[length//2]
    if mid1 == mid2:
        print("The middle elements are the same")
    else:
        print("The middle elements are different")
else:
    print("You did not enter an even number of items")