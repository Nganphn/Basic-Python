# Get input from user
number = int(input("Input an interger: "))
number2 = int(input("Input another interger: "))
number3 = int(input("One more: "))

# Implement conditions
if number >= number2 and number >= number3:
    print("Max value:", number)
elif number2 >= number and number2 >= number3:
    print("Max value:", number2)
else:
    print("Max value:", number3)