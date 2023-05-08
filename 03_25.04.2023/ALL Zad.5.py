"""
Stwórz grę ciepło zimno.
Komputer losuje liczbę z zakresu od 1 do 100.
Użytkownik podaje swój traf.
Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
Jeśli użytkownik zgadnie wygrywa gracz.
Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
"""
import random

computer = random.randrange(1, 101)

for i in range(0, 6):
    user_number = int(input("Select a number from 0 to 100 -->  "))

    if user_number == computer:
        print("Congrat, YOU WIN !")
        break
    elif 0 < user_number < computer and i < 6:
        print("Warm")
    elif computer < user_number < 100 and i < 6:
        print("Cold")
if computer == user_number:
    print("You win")
else:
    print("Correct number: ", computer, "Your number: ", user_number,
          "You lose")