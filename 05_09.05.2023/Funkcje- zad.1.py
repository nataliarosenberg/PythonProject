r = int(input("Podaj promien koła: "))

#pi * r^2
def calc_area(radius):
    pi = 3.14
    area = pi *radius **2
    return area

print(" Pole koła = ", calc_area(r))