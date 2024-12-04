import datetime
# from helper import sub
from helper import *

function_info()

number = print_and_return_number()
print("print_and_return_number:", number)

number = sum(number, 11)
print("Sum returneed:", number)

text = "Hello World!"
modify_text(text)
print(text)

number = sub(5, 11)
print("sub:", number)