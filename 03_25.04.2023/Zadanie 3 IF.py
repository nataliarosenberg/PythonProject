"""Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi."""

opinia1 = int(input("W skali 1-10 oceń tematykę książki:"))
opinia2 = int(input("W skali 1-10 oceń fabułę książki:"))
opinia3 = int(input("W skali 1-10 oceń okładkę książki:"))

ocena = (opinia1 + opinia2 + opinia3)/3

if ocena >= 7:
    print("bardzo dobra")
elif ocena >= 4:
    print("przeciętna")
else:
    print("nie warta uwagi")
