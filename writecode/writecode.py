# import the date to show curreent date and time
import datetime

def increase_number(x):
    """purpose of this fuction is to increase the given parameter 'x' by one

    Parameters
    ----------
    x : int
        a numeric value that will be increased by one

    Returns
    -------
    int
        increases parameter 'x' by one and returns the result from the function
    """

    return x + 1

# print current date and time
print(datetime.datetime.now())

# declare a variable as 'name' and assign some text into it
name = "Jani Immonen"

#print the contents of the 'name' variablee
print(name)

# call the function
value = increase_number(100)
print(value)