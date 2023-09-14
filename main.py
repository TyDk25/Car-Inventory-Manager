from typing import List, Optional, Union
import random


class Car:
    def __init__(self, car_type: str, make: str, engine_size: float, fuel_type: str, id: None):
        self.id: Optional[int] = id
        self.car_type: str = car_type
        self.make: str = make
        self.engine_size: float = engine_size
        self.fuel_type: str = fuel_type
        self.price: int = self.generate_random_price()

    @staticmethod
    def generate_random_price() -> int:
        return random.randint(1000, 10000)

    def __str__(self) -> str:
        return f'Car Type: {self.car_type}, Make: {self.make}, Engine Size: {self.engine_size}, Fuel Type: {self.fuel_type}, Price: £{self.price}'


class Inventory:
    def __init__(self) -> None:
        self.inventory: List[Car] = []
        self.next_car_id: int = 1

    def add_car(self, car) -> None:
        if car.id is None:
            car.id = self.next_car_id
            self.next_car_id += 1
            self.inventory.append(car)
            if car not in self.inventory:
                print(f'Car Make: {car.make}, Fuel Type: {car.fuel_type} has been added to the inventory.')

    def remove_car(self, car) -> Union[str, None]:
        if car in self.inventory:
            self.inventory.remove(car)
            print(f'Car ID: {car.id}, Car Make: {car.make} Fuel Type: {car.fuel_type} has been removed from the inventory.')
            return f'Car with ID of {car.id} not found in the inventory.'

    def filter_by_car_type(self, car_type: str) -> None:
        filtered_cars = [car for car in self.inventory if car.car_type == car_type]
        for car in filtered_cars:
            print(car)

    def view_inventory(self) -> None:
        for car in self.inventory:
            print(car)


inventory = Inventory()

car1 = Car('Hatchback', 'BMW', 2.0, 'Petrol', None)
car2 = Car('Hatchback', 'Audi', 2.0, 'Petrol', None)
car3 = Car('Motorcycle','Yahama',1.0,'Diesel',None)

inventory.add_car(car1)
inventory.add_car(car2)

inventory.remove_car(car1)
inventory.view_inventory()
