# while loop example
number = 10
while number >= 0:
    print(number)
    number -= 1

# for loop with range
number = 10
while number >= 0 and number < 100:
    print(number)
    number -= 1

# for loop with range
for number in range(10):
    print("Looping range(10):", number)

# for loop with range and start value
for i in range(5, 10):
    print("Looping range(5, 10):", i)

# for loop with range, step, and start value
for i in range(0, 10, 2):
    print("Looping range(0, 10, 2):", i)

# for loop over a string
for character in "Basics of programming with Python":
    print(character)

# for loop over a list
names = ["John", "Cherry", "Jack"]
for name in names:
    print(name)

# while loop with break
print("Running a while loop with break")
number = 0
while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        break # Exit the loop
    print("You entered:", number)

#while loop with break and continue
print("Running a while loop with continue")
number = 0
while True:
    number = int(input("Enter a number (0 to exit, 100 ignored): "))
    if number == 0:
        break # Exit the loop
    elif number == 100:
        print("Ignored")
        continue # Skip the rest of the loop and start the next iteration
    print("You entered", number)