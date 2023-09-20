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
    def __init__(self, car_type: str, make: str, engine_size: float, fuel_type: str, car_id: int = None):
        """
        Creates a new car object given the car type, make, engine size, fuel type & car id.
        :param car_type: The type of the car (e.g. hatchback, SUV)
        :param make: The make of the car (e.g. Renault)
        :param engine_size: The size of the engine in litres.
        :param fuel_type: The fuel type the car takes (e.g. petrol, deisel)
        :param number_plate: The number plate of the car.
        """
        self.car_id: int = car_id  # TODO Maybe we should make the car class auto create it's own ID (like numberplates)
        self.car_type: str = car_type
        self.make: str = make
        self.engine_size: float = engine_size
        self.fuel_type: str = fuel_type
        self.price: int = random.randint(1000, 20000)

    def __str__(self) -> str:
        """
        Returns a string representation of the Car object.
        :return: str The car represented in a string.
        """
        return f'Car ID: {self.car_id}, Car Type: {self.car_type}, Make: {self.make}, ' \
               f'Engine Size: {self.engine_size}, Fuel Type: {self.fuel_type}, Price: £{self.price}'


if __name__ == '__main__':
    # ONLY RUNS IF WE RUN THIS FILE DIRECTLY
    car1 = Car('Hatchback', 'BMW', 2.0, 'Petrol', None)
    car2 = Car('Hatchback', 'Audi', 2.0, 'Petrol', None)
    car3 = Car('Motorcycle', 'Yamaha', 1.0, 'Diesel', None)

    # inventory.add_car(car1)
    # inventory.add_car(car2)
    # inventory.add_car(car3)
    #
    # inventory_filter.by_price()
