from billing_service import Biller
from factories.spot_service_factory import SlotManagerFactory
from factories.vehicle_factory import VehicleFactory
from enums import SlotReservationStrategy, VehicleType
from parking import Parking


def main():
    # Programming to the implementation
    parking = Parking("MGF")

    parking.set_slot_manager(
        SlotManagerFactory.create_slot_manager(SlotReservationStrategy.MATCH_ONLY)
    )
    parking.set_biller(Biller)
    incoming_car = VehicleFactory.create_vehicle(VehicleType.CAR)
    
    parking_ticket = parking.get_parking_ticket(incoming_car)
    
    charges = parking.get_charges(parking_ticket)
    print(parking_ticket, charges)


main()
# Design principles

# Encapsulate parts that can change
# Program to an interface not to the implementation
# Prefer composition over inheritance
# Objects to interact with each other loosely
