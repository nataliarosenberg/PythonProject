"""Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie.
Sprawdź czy to samo zwróci Python.
"""
wiek = 36
print(bin(wiek ))

"""
Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. 
Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).
"""
bin_num = "1001111"
print(0b1001111)
print("Binarny na dziesiętny", bin_num,":",int(bin_num,2))

""""
Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym."""
hex_num = "1DB"
oct_num = "2063"
print("Octal to decimal",oct_num, " : ", int(oct_num,8))
print("Hexadecimal to decimal",hex_num, ":", int(hex_num,16))