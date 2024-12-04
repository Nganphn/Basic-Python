number = int(input("Gimme a number: "))
if number == 10:
    print("Number is 10")
elif number < 10:
    print("Number is less than 10")
elif number >= 20:
    print("Number is greater than or equal to 20")
else:
    print("Number is in between 11 and 19")

# Use and & or operators within conditions
number = int(input("Gimme a number: "))
if number > 0 and number < 10:
    print("Number iis in between 1 and 9")
elif number >= 10 or number == 0:
    print("Number is 10 or greater, or number is 0")

# Use both and & or operators within conditions
number = int(input("Gimme a number: "))
if (number > 0 and number < 10) or (number > 10 or number == 0):
    print("Number is in between 1 and 9, or number is greater than 10, or number is 0")

# Use pass for empty conditional block
number1 = 4
number2 = 43
if number1 > number2:
    pass