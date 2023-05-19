"""5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji."""

import random

computer = random.randrange(0, 101)
round= int(input("How many round you want to play > "))

def hot_cold (comp,user, round):
    if user == comp:
        print("Congratulation, you win")
    elif 0 < user_number < computer and i < int(round):
        print("Cold")
    elif computer < user_number < 100 and i < int(round):
        print("Hot")




for i in range(0, round):
    user_number = int(input("select a number from 0 to 100 -->  "))
    print(hot_cold(computer, user_number, round))
if computer == round:
    print("You win")
else:
    print("Sorry you lose computer choose number: ",computer)