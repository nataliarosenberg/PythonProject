'''dystans = 120
spalanie = 6.4
cena = 5.04

koszt = ((dystans * spalanie) /100) * cena
print(koszt)
'''

''''zadanie 2 '''

trasa = float(input("Podaj długość trasy: "))
spalanie = float(input("Podaj średnie spalanie na 100 km: "))
cena = float(input("Podaj cene benzyny: "))

cost = (trasa / 100) * spalanie * cena
print("Koszt podróży to ", round(cost,2))


