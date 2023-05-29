filename = "pan tadzio.txt"
with open(filename, 'r') as f:
    content = f.readlines()
    print(content)


print("---------------")

try:
    with open("text.txt", "x") as file:
        file.write("Hello world")
except FileExistsError:
    print("plik juz istnieje")