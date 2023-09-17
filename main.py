from typing import List, Optional, Union
import random


class Car:
    def __init__(self, car_type: str, make: str, engine_size: float, fuel_type: str, id: Optional[int] = None):
        self.id: Optional[int] = id
        self.car_type: str = car_type
        self.make: str = make
        self.engine_size: float = engine_size
        self.fuel_type: str = fuel_type
        self.price: int = self.generate_random_price()

    @staticmethod
    def generate_random_price() -> int:
        return random.randint(1000, 20000)

    def __str__(self) -> str:
        return f'Car Type: {self.car_type}, Make: {self.make}, Engine Size: {self.engine_size}, Fuel Type: {self.fuel_type}, Price: £{self.price}'


class Inventory:
    def __init__(self) -> None:
        self.inventory: List[Car] = []
        self.next_car_id: int = 1

    def add_car(self, car: Car) -> None:
        if car.id is None:
            car.id = self.next_car_id
            self.next_car_id += 1
        self.inventory.append(car)
        print(f'Car Make: {car.make}, Fuel Type: {car.fuel_type} has been added to the inventory.')

    def remove_car(self, car: Car) -> Union[str, None]:
        if car in self.inventory:
            self.inventory.remove(car)
            print(f'Car ID: {car.id}, Car Make: {car.make} Fuel Type: {car.fuel_type} has been removed from the inventory.')
        else:
            return f'Car with ID of {car.id} not found in the inventory.'

    def view_inventory(self) -> None:
        for car in self.inventory:
            print(car)


class FilterClass(Inventory):
    def __init__(self, inventory: Inventory):
        self._ = inventory

    def filter_by_car_type(self, car_type: str) -> None:
        filtered_cars = [car for car in self._.inventory if car.car_type == car_type]
        for car in filtered_cars:
            print(car)

    def filter_by_make(self, make: str) -> None:
        filtered_make = [car for car in self._.inventory if car.make == make]
        for car in filtered_make:
            print(car)
    def filter_by_fuel_type(self,fuel_type:str)-> None:
        filtered_fuel = [car for car in self._.inventory if car.fuel_type == fuel_type]
        for car in filtered_fuel:
            print(car)
    def filter_by_engine_size(self,engine_size:float)-> None:
        filter_engine_size = [car for car in self._.inventory if car.engine_size == engine_size]
        for car in filter_by_engine_size:
            print(car)
    def under_10k(self)-> None:
        filtered_under_10k = [car for car in self._.inventory if car.price <= 10000]
        for car in filtered_under_10k:
            print(car)



inventory = Inventory()


filter = FilterClass(inventory)

car1 = Car('Hatchback', 'BMW', 2.0, 'Petrol', None)
car2 = Car('Hatchback', 'Audi', 2.0, 'Petrol', None)
car3 = Car('Motorcycle', 'Yamaha', 1.0, 'Diesel', None)

inventory.add_car(car1)
inventory.add_car(car2)
inventory.add_car(car3)

inventory.view_inventory()

print("\nFiltering by Price':")


filter.filter_by_make('BMW')
