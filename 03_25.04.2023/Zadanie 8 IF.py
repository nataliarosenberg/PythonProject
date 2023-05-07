"""
Sortowanie.
Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.
"""
num_1 = int(input("Enter first number--> "))
num_2 = int(input("Enter second number--> "))
num_3 = int(input("Enter third number--> "))
maximum=max(num_1,num_2,num_3)

print("Before sorting: ", num_1, num_2, num_3)
print("The biggest number", maximum)

if num_1 < num_2 < num_3:
    print("After sorting", num_1, num_2, num_3)
elif num_1 < num_3 < num_2:
    print("After sorting: ", num_1, num_3, num_2)
elif num_2 < num_1 < num_3:
    print("After sorting: ", num_2, num_1, num_3)
elif num_2 < num_3 < num_1:
    print("After sorting: ", num_2, num_3, num_1)
elif num_3 < num_1 < num_2:
    print("After sorting: ", num_3, num_1, num_2)
else:
    print("After sorting: ", num_3, num_2, num_3)