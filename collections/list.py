# declare a list of numbers and initialize
list = [5, 10, 15]
print(list)

# append adds new item to the end of the list
list.append(100)  # Adds 100 to the end of the list
print(list)

# insert new item to the middle of the list
list.insert(1, 7)  # Inserts 7 at index 1
print(list)

# list items can be accessed via [] operator
# note that index in [] is zero based
print("List item at index 1:", list[1])  # Output: 7

# index to access list can be negative
# negative index means beginning from the end of the list
print("List item at index -1:", list[-1])  # Output: 100

# index can also be specified as a range
# range parameters are start index (inclusive) and end index (exclusive)
print("List items at range 1:4:", list[1:4])  # Output: [7, 10, 15]

# # list item can be changed with [] operator
# list[1] = 60
# print("List contents after modification:", list)  # Output: [5, 60, 10, 15, 100]

# remove item from the list
# only a first occurrence of the item is removed
list.remove(10)
print("List contents after 10 was removed:", list)  # Output: [5, 60, 15, 100]

# pop function allows to remove a specific item
value = list.pop(1)
print("list.pop(1) returned:", value)  # Output: 60
print("List contents after pop(1):", list)  # Output: [5, 15, 100]

# another way to remove item at index is 'del'
del list[1]
print("List contents after del list[1]:", list)  # Output: [5, 100]

# clear removes all items from the list
list.clear()
print("List contents after clear:", list)  # Output: []


# declare list of names and print
namelist = ["Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"]
print(namelist)

# loop thru a list
for name in namelist:
    print(name)

# use 'len' function to determine list length
print("namelist length is:", len(namelist))  # Output: 6

# check if item exists
if "Liam" in namelist:
    print("Yes, 'Liam' is in the names list")

# note that modifying the 'anothernamelist' also modifies the 'namelist'
# as both variables reference the same list
anothernamelist = namelist
anothernamelist[0] = "Roger"
print(namelist)  # Output: ['Roger', 'Sally', 'Liam', 'Robert', 'Emma', 'Isabella']

# if you need another copy, use the list copy function
anothernamelist = namelist.copy()
anothernamelist[0] = "Harris"
anothernamelist[-1] = "Mary"
print("Contents of namelist:", namelist)  # Output: ['Roger', 'Sally', 'Liam', 'Robert', 'Emma', 'Isabella']
print("Contents of anothernamelist:", anothernamelist)  # Output: ['Harris', 'Sally', 'Liam', 'Robert', 'Emma', 'Mary']

# join list to another
combinedlist = namelist + anothernamelist
# another way is to use list 'extend' function
# combinedlist = namelist.copy()
# combinedlist.extend(anothernamelist)
print("Contents of combinedlist:", combinedlist)
