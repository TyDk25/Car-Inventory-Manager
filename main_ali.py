from CarShop.car import Car
from CarShop.inventory import Inventory
import operator  # functions look like eq(10, 10) -> True | gt(10, 15) -> False  || short for equal and greater than


car1 = Car('Hatchback', 'BMW', 2.0, 'Petrol', None)
car2 = Car('Hatchback', 'Audi', 2.0, 'Petrol', None)
car3 = Car('Motorcycle', 'Yamaha', 1.0, 'Diesel', None)
car4 = Car('Lorry', 'Renault', 28.0, 'Diesel', None)
print("Adding cars to inventory----------------------------")
inventory: Inventory = Inventory()
inventory.add_car(car1)
inventory.add_car(car2)
inventory.add_car(car3)
inventory.add_car(car3)
inventory.add_car(car4)

print()
print("Viewing cars with price > 500---------------------------")
inventory.view_by('price', 500, operator.gt)
print()
print("Viewing cars with type Hatchback --------------------------")
inventory.view_by('car_type', 'Hatchback', operator.eq)  # Eq is default behaviour but just showing you expample
print()
print("Viewing cars with type Hatchback again --------------------------")
inventory.view_by('car_type', 'Hatchback')  # Showing you dont need to repeat the default arg
