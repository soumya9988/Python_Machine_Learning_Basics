from abc import ABCMeta, abstractmethod

class Vehicle:

    base_price = 0.0

    def __init__(self, model, year, miles, purchase_date):
        self.model = model
        self.year = year
        self.miles = miles
        self.purchase_date = purchase_date

    def calculate_price(self):
        return self.base_price - 0.1 * self.miles

    @abstractmethod
    def vehicle_type(self):
        pass


class Car(Vehicle):
    base_price = 10000

    def vehicle_type(self):
        return 'Car'


class Truck(Vehicle):
    base_price = 12000

    def vehicle_type(self):
        return 'Truck'


alto = Car('SUV', 1999, 34789, 12122018)
print('The current market value is ', alto.calculate_price())
print(alto.vehicle_type())