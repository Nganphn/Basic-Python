from vehicle import Vehicle

datsun = Vehicle("Datsun", "100A", 998, 12)
print(datsun)

toyota = Vehicle("Toyota", "Surpa", 2997, 175)
print(toyota)

print("datsun hp:", round(datsun.hoursepower(), 2))
print("toyota hp:", round(toyota.hoursepower(), 2))