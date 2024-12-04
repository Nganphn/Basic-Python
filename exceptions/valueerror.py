
fruits = ['apple', 'banana', 'coconut', 'durian', 'elderberry']

while True:
    try:
        index = int(input("Enter the index in the list you want to modify: "))
        if 0 <= index < 5:
            break
        else:
            print("Out-range index, enter a number from 0 to 4")
    except ValueError:
        print("Invalid type of index, enter a number from 0 to 4")

fruits[index] = input("Type the fruit you'd like to replace: ")

print("Updated list of fruits:", fruits)