age = int(input("What is your age? "))
if age < 13:
    print("child")
elif age > 12 and age < 20:
    print("teen")
elif age > 19 and age < 65:
    print("adult")
else:
    print("senior")