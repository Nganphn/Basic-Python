try:
    animals = ['mouse', 'cat', 'dog', 'monkey']

    animals[4] = 'pig'
    print("Animals after modification: ", animals)
except IndexError:
    print('Index is used for modification does not exist. The list remains unchanged:', animals)