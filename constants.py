from enums import VehicleType, ParkingSlotType


class VehicleTypeParkingSlotTypeMatch:
    veh_type_slot_type_map = {VehicleType.CAR: ParkingSlotType.CAR, VehicleType.BIKE: ParkingSlotType.BIKE}

    @classmethod
    def get_fitting_slot_type(cls,vehicle_type):
        return cls.veh_type_slot_type_map[vehicle_type]
