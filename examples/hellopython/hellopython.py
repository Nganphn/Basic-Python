# import a datetime module to access current date and time
import datetime

# declare a variable named 'msg' and set some text into it
msg = "This program was run by Jani Immonen"

# print the contents of 'msg' variable into Console
print(msg)

# print the current date and time
print(datetime.datetime.now())

# read text from Console and echo back
text = input("Enter some text: ")
print("you wrote:")
print(text)