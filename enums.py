from enum import Enum


class ParkingSlotType(Enum):

    CAR = "CAR"
    BIKE = "BIKE"


class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"


class SlotReservationStrategy(Enum):
    MATCH_ONLY = "Match Only"
    MATCH_PLUS = "Match Plus"
