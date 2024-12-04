# Declare the start balance
start_balance = 2000
print("Bank account balance:", start_balance, "€")

# Get inputs from user as intergers
euros = int(input("How many euros will be added to the balance? "))
cents = int(input("How many cents will be added to the balance? "))

# Print the current account balanace
current_balance = start_balance + euros + (cents / 100)
print("Bank account balance:", current_balance, "€")