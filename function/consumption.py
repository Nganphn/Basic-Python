from utils import *

distant = float(input("Enter trip length in km: "))
price = float(input("Enter fuel price/liter: "))
fuel = float(input("Enter fuel consumption/100 km: "))

fuel_consumed = calc_consumption(distant, price, fuel)
print("fuel consumed: ",fuel_consumed)

cost = fuel_consumed * price
print("Cost: ", cost, "€")