"""
Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c)
"""

def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2

 #lub opcja taka
    # if val1 > val2:
    #    return val1
    # else:
    #    return val2

def maximum_of(a,b,c):
    tmp = max_of_two(a, b)
    return max_of_two(c,tmp)

def main():
# głowny kod
    x,y,z = [5,13,2]
    result = maximum_of(x,y,z)
    print(result)

main()



""""
numbers = ("1", "10", "25")
numbers_to_set = set(numbers)

maximum_of_list = max(numbers_to_set)
print(maximum_of_list)

# 2

a, b, c = [5, 13, 2]

tmp = ''

if a> b:
    tmp= a
else:
    tmp = b
    
if c> tmp:
    print('najwieksza wartosc to', c)
else:
    print('najwieksza wartosc to', tmp)
"""

