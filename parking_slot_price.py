from enums import VehicleType


class ParkingSlotPrice:

    @classmethod
    def get_price(cls, vehicle_type):
        if vehicle_type == VehicleType.CAR:
            return cls(100, 200)
        else:
            return cls(5, 60)

    def __init__(self, min_charge, hourly_charge):
        self.min_charge = min_charge
        self.hourly_charge = hourly_charge
