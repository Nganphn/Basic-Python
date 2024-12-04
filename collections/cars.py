
# list of dictionaries
cars = [
    {'registration': 'JKL-456', 'make': 'Toyota'}, # Toyota
    {'registration': 'MNO-789', 'make': 'Honda'}, # Honda
    {'registration': 'PQR-012', 'make': 'Ford'},
    {'registration': 'STU-345', 'make': 'Chevrolet'},
    {'registration': 'VWX-678', 'make': 'BMW'},
    {'registration': 'YZA-901', 'make': 'Audi'},
    {'registration': 'BCD-234', 'make': 'Mercedes-Benz'},
    {'registration': 'EFG-567', 'make': 'Volkswagen'},
    {'registration': 'NOP-456', 'make': 'Toyota'},  # Toyota
    {'registration': 'QRS-789', 'make': 'Honda'}    # Honda
]

# alphabetical order by car brand
print("Cars sorted by registration")
sorted_by_reg = sorted(cars, key=lambda x: x['registration'])
for car in sorted_by_reg:
    car_str = f"registration: {car['registration']}, make: {car['make']}"
    print(car_str)
print()

# alphabetical order by registration number
print("Cars sorted by make")
sorted_by_make = sorted(cars, key=lambda x: x['make'])
for car in sorted_by_make:
    car_str = f"registration: {car['registration']}, make: {car['make']}"
    print(car_str)