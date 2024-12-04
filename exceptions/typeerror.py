# when '0' is called, the function returns True because the value is zero
# when '1' and '2.3' are called, the function returns False because the values are non-zero numbers
# when 'num' is called, the fuction raises a TypeError because the value is not a number (int or float)
# the except block catches the TypeError in 'ex' and prints 'ex' as an error message

def isthiszero(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Parameter is not a number")
    if num == 0:
        return True
    else:
        return False

try:
    print(isthiszero(0))
    print(isthiszero(1))
    print(isthiszero(2.3))
    print(isthiszero('num'))
except TypeError as ex:
    print(ex)

