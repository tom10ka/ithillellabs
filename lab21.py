import datetime


class Car:
    def __init__(self, producer: str, brand: str, fuel_expense: float, release=2020) -> None:
        self.release = release
        self.producer = producer
        self.brand = brand
        self.fuel_expense = fuel_expense
        self._race = 0

    def __str__(self) -> str:
        return f'Release: {self.release}, {self.producer}, brand: {self.brand}, {self.fuel_expense}, {self._race}'

    @property
    def car_age(self):
        age = datetime.datetime.today().year - self.release
        return f'Your cars age is {age}'


new_car1 = Car('Honda', 'Civic', 3.4)
print(new_car1)
print(new_car1.car_age)

new_car2 = Car('Volkswagen', 'Audi', 3.8, 2021)
print(new_car2)
print(new_car2.car_age)

new_car3 = Car('Hyundai', 'Accent', 2.4, 1992)
print(new_car3)
print(new_car3.car_age)
