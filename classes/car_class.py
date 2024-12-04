class Car:

    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
        Car.total_price += price # Add the car price to the total_price when a new car is created

    def __str__(self):
        return self.brand + " " + self.model + " " + str(self.price)

    # Class-level variable to store the sum of prices
    total_price = 0

    # Define a method that is bound to the class that can access the class-level variable
    @classmethod
    def get_total_price(cls):
        return cls.total_price

    brand = ""
    model = ""
    price = 0