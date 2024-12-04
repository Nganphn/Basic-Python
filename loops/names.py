# get input from user
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

# calculate number of characters
num_chatacters = len(first_name)

# extract first character of first name
c1 = first_name[0]

print(c1 * num_chatacters, end=' ') # end=' ' to end with a space, not line break

print(last_name[::-1]) # print character in reserve order

# # using loop
# while num_chatacters > 0:
#     print(c1, end='')
#     num_chatacters -=1

# print(" ", end='')

# print(last_name[::-1])