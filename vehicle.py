from enums import VehicleType


class Vehicle:

    def get_type(self):
        return self.type


class Car(Vehicle):
    type = VehicleType.CAR


class Bike(Vehicle):
    type = VehicleType.BIKE
