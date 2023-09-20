"""
   Inventory represents a collection of cars that a shop might keep.
"""
from CarShop.car import Car
from typing import Any, Callable
import operator


class Inventory:

    def __init__(self) -> None:
        """
        Creates a new inventory object.
        """
        self.inventory: list[Car] = []
        self.__current_car_id: int = 0

    @property
    def next_car_id(self) -> int:
        """
        Returns the next available car ID (incremental)
        :return:
        """
        self.__current_car_id += 1
        return self.__current_car_id

    # Adds a car into the inventory if the id does not already exist, increases the id by one each time.
    def add_car(self, car: Car) -> None:
        """
        Adds a car into the inventory. Car will not be duplicated if already present. If the car has no ID, the function
        will add one for it.
        :param car: Car
        :return:
        """
        if car.car_id is None:  # If no ID, give it one
            car.car_id = self.next_car_id

        inventory_car_ids = {car.car_id for car in self.inventory}  # What IDs do we have already (set)

        if car.car_id not in inventory_car_ids:  # Add if not present
            self.inventory.append(car)
            print(f'Car Make: {car.make}, Fuel Type: {car.fuel_type} has been added to the inventory.')
        else:
            print(f'Car with matching ID ({car.car_id}) already in inventory!')

    def remove_car(self, car: Car) -> None:
        """
        Removes a car into the inventory if the id exists, returns a message if the id is not found
        :param car: The car to remove.
        :return:
        """
        try:
            self.inventory.remove(car)
            print(
                f'Car ID: {car.car_id}, Car Make: {car.make}, '
                f'Fuel Type: {car.fuel_type} has been removed from the inventory.')
        except ValueError:
            print(f'Car ID: {car.car_id} could not be found in the inventory.')
            pass

    def view_inventory(self) -> None:
        """
        Prints each of the cars in the inventory.
        :return:
        """
        for car in self.inventory:
            print(car)

    def view_by(self, attribute: str, filter_value: Any, relate: Callable = operator.eq) -> None:
        """
        Allows the user to filter the inventory given an attribute of car, the value to filter on, and the operator
        resulting in true.
        :param attribute: The attribute of Car to filter on (e.g. car_id)
        :param filter_value: The to filter for.
        :param relate: The relation of the attribute to the filter value (e.g. equal, greater than; use operators mod)
        :return:
        """
        cars = filter(lambda c: relate(getattr(c, attribute), filter_value), self.inventory)
        for car in cars:
            print(car)
