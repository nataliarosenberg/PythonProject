import random

'''Użytkownik podaje jedną z 3 figur.

Komputer losuje jedną z 3 figur.

Sprawdź kto wygrał tę rundę.

Zmień kod tak, by użytkownik mógł podac liczbę rund.

Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

'''

wins = 0
numgames = int(input("ile razy chcesz zagrać?: "))

for _ in range(numgames):
    choice = input("twój ruch (rock/paper/scissors): ")
    computerchoice = random.choice(["rock","paper","scissors"])
    if choice == "end": break
    print(f"Komputer wybrał {computerchoice}")
    if choice == "rock":
        if computerchoice == "paper": print("Komputer wygrywa")
        elif computerchoice == "scissors":
            print("Wygrałeś!")
            wins += 1
        else: print("Remis")
    elif choice == "paper":
        if computerchoice == "scissors": print("Komputer wygrywa")
        elif computerchoice == "rock":
            print("Wygrałeś!")
            wins += 1
        else:
            print("Remis")
    elif choice == "scissors":
        if computerchoice == "rock": print("Komputer wygrywa")
        elif computerchoice == "paper":
            print("Wygrałeś!")
            wins += 1
        else:
            print("Remis")

    else: print("Złe dane")

print(f"Wygrałeś {wins} razy")