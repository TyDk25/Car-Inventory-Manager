# Used to document variables, strings
from typing import List, Optional, Union
# Used to generate random prices
import random

# Class: Car holds information about Cars, also an id which is passed as None to generate a random id.
class Car:

    """
    Represents a car object.
    Attributes:
        car_type (str): The type or category of the car.
        make (str): The car's manufacturer or brand.
        engine_size (float): The size of the car's engine.
        fuel_type (str): The type of fuel the car uses (e.g., petrol, diesel).
        id (Optional[int]): An optional unique identifier for the car. If not provided, a random ID is generated.
    """
    def __init__(self, car_type: str, make: str, engine_size: float, fuel_type: str, id: Optional[int] = None):
        self.id: Optional[int] = id
        self.car_type: str = car_type
        self.make: str = make
        self.engine_size: float = engine_size
        self.fuel_type: str = fuel_type
        self.price: int = self.generate_random_price()

    '''
    Static Method: generate_random_price() generates a random price for the self.price attribute. Static method as it is not specific to the Class.
    '''
    @staticmethod
    def generate_random_price() -> int:
        return random.randint(1000, 20000)


    #def __str__ returns information about the Car Types
    def __str__(self) -> str:
        return f'Car Type: {self.car_type}, Make: {self.make}, Engine Size: {self.engine_size}, Fuel Type: {self.fuel_type}, Price: £{self.price}'

'''
Holds information about the instances of Cars.
    Methods:
    __init__: initializes self.inventory list and assigns and id of 1.
    
    add_car: adds car to inventory list if id is already found within the list.
    
    remove_car: removes car from the inventory if the id exists
    
    view_car: iterates over the inventory list and prints the cars that are currently found
    
     
'''
class Inventory:

    # def __init__ holds self.inventory list and an integer of 1 for the car id which is iterated in the add_car function
    def __init__(self) -> None:
        self.inventory: List[Car] = []
        self.next_car_id: int = 1

# Adds a car into the inventory if the id does not already exist, increases the id by one each time.
    def add_car(self, car: Car) -> None:
        if car.id is None:
            car.id = self.next_car_id
            self.next_car_id += 1
        self.inventory.append(car)
        print(f'Car Make: {car.make}, Fuel Type: {car.fuel_type} has been added to the inventory.')

# Removes a car into the inventory if the id exists, returns a message if the id is not found
    def remove_car(self, car: Car) -> Union[str, None]:
            if car in self.inventory:
                self.inventory.remove(car)
                print(f'Car ID: {car.id}, Car Make: {car.make}, Fuel Type: {car.fuel_type} has been removed from the inventory.')
            else:
                return (f'Car with ID of {car.id} not found in the inventory.')

# Iterates over the inventory list and prints the cars that are within the inventory
    def view_inventory(self) -> None:
        for car in self.inventory:
            print(car)

'''
class FilterClass: Inherits from Inventory class to enable filtering of the inventory.
    Methods:
    __init__: intiializes the Inventory class
    
    by_car_type 
    by_make
    by_fuel_type
    by_engine_size
    by_price
    
    These methods filter the inventory list by parameters that the user inputs e.g. car_type which then matches the attributes defined in the Car Class.
    
'''
class FilterInventory(Inventory):

    # __init__ method intializes the inventory class
    def __init__(self, inventory: Inventory):
        self._ = inventory

# The following functions use list comprehension to check if the car_type attribute is equivalent to the parameter that is relative to the function that is passed in.
    def by_car_type(self, car_type: str) -> None:
        print(f'Filtering By {car_type}:')
        filtered_cars = [car for car in self._.inventory if car.car_type == car_type]
        for car in filtered_cars:
            print(car)
    def by_make(self, make: str) -> None:
        filtered_make = [car for car in self._.inventory if car.make == make]
        for car in filtered_make:
            print(car)
    def by_fuel_type(self,fuel_type:str)-> None:
        filtered_fuel = [car for car in self._.inventory if car.fuel_type == fuel_type]
        for car in filtered_fuel:
            print(car)
    def by_engine_size(self,engine_size:float)-> None:
        filter_engine_size = [car for car in self._.inventory if car.engine_size == engine_size]
        for car in filter_engine_size:
            print(car)

    def by_price(self)-> None:
        price_to_filter = int(input('Enter a price you would like to filter by: '))
        filtered_under_10k = [car for car in self._.inventory if car.price <= price_to_filter]

        if not filtered_under_10k:
            print (f'No Cars found under £{price_to_filter}')
        else:
            for car in filtered_under_10k:
                print(car)


inventory = Inventory()
inventory_filter = FilterInventory(inventory)

car1 = Car('Hatchback', 'BMW', 2.0, 'Petrol', None)
car2 = Car('Hatchback', 'Audi', 2.0, 'Petrol', None)
car3 = Car('Motorcycle', 'Yamaha', 1.0, 'Diesel', None)

inventory.add_car(car1)
inventory.add_car(car2)
inventory.add_car(car3)

inventory_filter.by_price()
