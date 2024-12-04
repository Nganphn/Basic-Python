number = 5
account_balance = 110.54
print(number)
print(account_balance)

number = 55
number2 = number + 2
print("number2 is", number2)
print("number2 is " + str(number2))

print("Type of 'number' is", type(number))
print("Type of 'account_balance' is", type(account_balance))

first_name = "Ngan"
last_name = "Pham"
full_name = first_name + " " + last_name
print(full_name)

age = 28
person = "First name: {}. Last name: {}. Age: {}".format(first_name, last_name, age)
print(person)

text = "ABC"
c1 = text[0]
c2 = text[1]
c3 = text[2]
print("Second char is " + c2)

print("Text length is " + str(len(text)) + " characters.")

text2 = "ABD"
if text == text2:
    print("Texts are identical")
else:
    print("Texts are different")


line = input("Please say something: ")
print("Thank you for saying this: " + line)

# line = input("Please say something: ")
# print("Thank you for saying this: " + line)

line = input("Enter a number: ")
number = float(line)
print("You entered:", number)