"""
Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
utwórz nowy łańcuch s3, dołączając s2 w środku s1.
"""
s1 = "automatyzacja"
s2 = "robotyka"
s1_mid = len(s1)//2
s3=s1[0:s1_mid] + s2 + s1[len(s1) //2: len(s1)]
print("Połączone s1 i s2 to: ", s3)
