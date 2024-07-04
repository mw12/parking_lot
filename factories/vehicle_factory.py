from enums import VehicleType
from vehicle import Bike, Car


class VehicleFactory:

    def create_vehicle(type):
        if not isinstance(type, VehicleType):
            raise ValueError()
        if type == VehicleType.CAR:
            return Car()
        elif type == VehicleType.BIKE:
            return Bike()
        else:
            raise NotImplementedError()
