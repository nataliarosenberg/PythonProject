"""1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for."""

fahr = 0
while fahr <= 200:
    celc = round(5 / 9 * (fahr - 32),2)
    print(celc)
    fahr += 20

