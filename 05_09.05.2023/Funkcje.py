def mood():
    print("How are you?")


print("lalala")
print("Dobry dzień")
mood()
mood()
"""
def my_mood(answear):
    print("My mood today:")
    print(answear)

resp = input("How are you?")
my_mood(resp)
"""
def my_mood2(answear):
    return answear *2
resp = input("How are you?")
twiced = my_mood2(resp)
print("My mood is like" , twiced)