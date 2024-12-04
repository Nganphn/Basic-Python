
import random

# define function lottery to generate 7 random numbers in range 1 - 40
def lottery():
    return random.sample(range(1, 41), 7) # 7 unique numbers
    """
    random.sample()
    • to generate randomly a list of unique items from a sequence/range/set

    random.sample(population, k)
    • population: sequence/range/set
    • k: number of unique items

    range (start, stop)
    • start inclusive
    • stop exclusive
    """

# get input from user
num_sets = int(input("How many sets of lotttery numbers to generate: "))

# run the fro loop with the number of num_sets
for _ in range(num_sets): # _ is the unused variable in the loop body, function lottery is used
    print(lottery())