from car_class import Car

car1 = Car("Skoda", "Octavia", 3000)
print("car1:", car1)

car2 = Car("Audi", "A4", 4000)
print("car2:", car2)

car3 = Car("Volvo", "V70", 5000)
print("car3:", car3)

print("Total price of the cars is", Car.get_total_price())

import random

# car brands
brands = ['Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo', 'VW']

# place holder of created car objects
car_collection = []

# Create 5 random car objects
for _ in range(5):
    brand = random.choice(brands)  # Randomly select a brand from the brand list
    model = "-"  # empty
    price = random.randint(1000, 10000)  # Randomly get a price between 1000 and 10000

    car = Car(brand, model, price)  # Create a Car object

    car_collection.append(car)  # Add the car to the collection

# Print information of all cars
for car in car_collection:
    print(car)