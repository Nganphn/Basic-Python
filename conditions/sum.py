# Get input from user
number1 = int(input("Input number: "))
number2 = int(input("Input number: "))
number3 = int(input("Input number: "))
number4 = int(input("Input number: "))
number5 = int(input("Input number: "))

# Apply addition
sum1 = number1 + number2 + number3 + number4 + number5

# Apply conditions
if number1 < 1:
    sum2 = sum1 - number1
    print("Sum is", sum2)
elif number2 < 1:
    sum2 = sum1 - number2
    print("Sum is", sum2)
elif number3 < 1:
    sum2 = sum1 - number3
    print("Sum is", sum2)
elif number4 < 1:
    sum2 = sum1 - number4
    print("Sum is", sum2)
elif number5 < 1:
    sum2 = sum1 - number5
    print("Sum is", sum2)
else:
    print("Sum is", sum1)