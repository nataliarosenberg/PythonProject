translate = [('apple', 'jablko'), ('ball', 'pilka')]
en_pl = dict(translate )
print(en_pl)

print(en_pl.pop('ball'))
print(en_pl)
en_pl.popitem()
print(en_pl)

grades = {}.fromkeys(['Math','English','Art'], 3)
print(grades)

print(list(sorted(grades.keys())))
print(tuple(sorted(grades.keys())))
print(set(sorted(grades.keys())))
