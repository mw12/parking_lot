from parking_ticket import ParkingTicket


class Parking:

    def __init__(self, name):
        self.name = name
        self.spot_service = None
        self.billing_service = None

    def set_slot_manager(self, spot_service):
        self.spot_service = spot_service

    def set_biller(self, billing_service):
        self.billing_service = billing_service

    def get_parking_ticket(self, vehicle):
        available_slot = self.spot_service.reserve_available_slot(vehicle)
        return ParkingTicket.create_parking_ticket(available_slot, vehicle)

    def get_charges(self, parking_ticket):
        return self.billing_service.get_charges(parking_ticket)
