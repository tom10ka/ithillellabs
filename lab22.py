from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, brand: str, volume: float, fuel_residue: float, speed: float, race: float):
        self.brand = brand
        self.volume = volume
        self.fuel_residue = fuel_residue
        self.speed = speed
        self.race = race

    @abstractmethod
    def __str__(self):
        pass

    def fuel_recharge(self, recharge_volume):
        refuel = self.fuel_residue + recharge_volume
        if refuel > self.volume:
            unused_fuel = refuel - self.volume
            return f'Fuel tank is full, unused fuel is {unused_fuel} litres'
        else:
            return f'Fuel tank is recharged, now its {refuel} litres in tank'

    def fuel_transfusion(self, other, transfusion_number):
        transfused_volume = self.volume - self.fuel_residue
        tranfusing_volume = other.fuel_residue
        if tranfusing_volume >= transfusion_number <= transfused_volume:
            other.fuel_residue -= transfusion_number
            self.fuel_residue += transfusion_number
            return f'Transfusing already done, residue in transfuser is {other.fuel_residue}, in transfused is ' \
                   f'{self.fuel_residue}'
        elif transfusion_number > tranfusing_volume:
            return f'Number of transfused fuel is more than transfuser transport has'
        else:
            return f'Number of transfused fuel is more than transfused transport has'


class Auto(Transport):
    def __init__(self, brand: str, volume: float, fuel_residue: float, speed: float, race: float, passenger_number: int,
                 safety_pillows: bool):
        super().__init__(brand, volume, fuel_residue, speed, race)
        self.passenger_number = passenger_number
        self.safety_pillows = safety_pillows

    def __str__(self):
        return f'Auto, brand is {self.brand}'


class Motorbike(Transport):
    def __init__(self, brand: str, volume: float, fuel_residue: float, speed: float, race: float, added_seat: bool):
        super().__init__(brand, volume, fuel_residue, speed, race)
        self.added_seat = added_seat

    def __str__(self):
        return f'Motorbike, brand is {self.brand}'
