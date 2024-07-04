from enums import ParkingSlotType


class ParkingSlot:

    @classmethod
    def get_best_available_slot(cls, slot_type):
        if slot_type == ParkingSlotType.CAR:
            return cls(ParkingSlotType.CAR, 0, 1)

        if slot_type == ParkingSlotType.BIKE:
            return cls(ParkingSlotType.BIKE, 0, 1)

    def __init__(self, type, floor, serial_number):
        self.reserved = False
        self.type = type
        self.floor = floor
        self.serial_number = serial_number

    def reserve(self):
        self.reserved = True


# class CarParkingSlot:
#     pass


# class BikeParkingSlot:
#     pass
