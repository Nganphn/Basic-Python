# declare tuple of names and print
nametuple = ("Joe", "Sally", "Liam", "Robert", "Emma", "Isabella")
print("Contents of nametuple is:", nametuple)

# # tuple items can be accessed via [] operator
# # note that index in [] is zero based
# print("Tuple item at index 1:", nametuple[1])

# # index to access tuple can be negative
# # negative index means beginning from the end
# print("Tuple item at index -1:", nametuple[-1])

# # index can also be specified as a range
# # range parameters are start index (inclusive) and end index (exclusive)
# print("Tuple items at range 2:5:", nametuple[2:5])

# items of the tuple cannot be modified after its declared, though
# it is possible to convert tuple to list, modify the list and
# convert list back to tuple
namelist = list(nametuple)
namelist[1] = "Mary"
nametuple = tuple(namelist)
print("Contents of nametuple is:", nametuple)

# note that on below the variable is not a tuple
nametuple = ("Joe")
print(nametuple)
print(type(nametuple))

# tuple with only one item must be declared with trailing comma
nametuple = ("Joe", )
print(nametuple)
print(type(nametuple))
