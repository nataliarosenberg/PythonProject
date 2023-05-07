# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

num_1 = int(input("Enter first number --> "))
num_2 = int(input("Enter second number --> "))

sum= num_1 + num_2

if sum > 100:
    print(" The sum of your numbers is: ", sum)
else:
    print("Koniec")