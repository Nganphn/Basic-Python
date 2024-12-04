try:
    number1 = 100
    number2 = 0
    result = number1 / number2
    print("Result is ", result)
except ZeroDivisionError:
    print("Can't divide by zero!")

try:
    number = int(input("Give a number: "))
    print("You entered: ", number)
except ValueError:
    print("Unable to convert to number")
except Exception as ex:
    print("Something else went wrong: ", ex)

try:
    number = [1, 2, 3, 4, 5]
    print("Last number is ", number[5])
except IndexError:
    print("Wrong index used in accessing list")  
  