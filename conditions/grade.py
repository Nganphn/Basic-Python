# Get input from user
point = int(input("Insert your points: "))

# Apply conditions
if point >= 0 and point < 2:
    print("Grade: 0")
elif point > 1 and point < 4:
    print("Grade: 1")
elif point > 3 and point < 6:
    print("Grade: 2")
elif point > 5 and point < 8:
    print("Grade: 3")
elif point > 7 and point < 10:
    print("Grade: 4")
elif point > 9 and point <= 12:
    print("Grade: 5")
else:
    pass