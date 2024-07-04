from datetime import datetime
from parking_slot_price import ParkingSlotPrice


class ParkingTicket:

    @classmethod
    def create_parking_ticket(cls, parking_slot, vehicle):
        pricing_rule = ParkingSlotPrice.get_price(vehicle.get_type())
        return cls(parking_slot, vehicle, pricing_rule)

    def __init__(self, parking_slot, vehicle, pricing_rule):
        self.start_time = datetime.now()
        self.parking_slot = parking_slot
        self.vehicle = vehicle
        self.pricing_rule = pricing_rule

    def get_start_time(self):
        return self.start_time

    def get_rates(self):
        return {
            "minimum_charge": self.pricing_rule.min_charge,
            "hourly_charge": self.pricing_rule.hourly_charge,
        }
