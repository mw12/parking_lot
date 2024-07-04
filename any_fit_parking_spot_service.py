from interfaces.parking_spot_service import SpotServiceInterface


class AnyFitParkingSpotService(SpotServiceInterface):

    def __init__(self, parking_slot_data_manager):
        self.parking_slot_data_manager = parking_slot_data_manager

    def reserve_available_slot(self, vehicle):
        fitting_slot_types = self.parking_slot_data_manager.get_fitting_slot_types(
            vehicle.get_type
        )
        available_slot = self.parking_slot_data_manager.get_best_available_slot(
            fitting_slot_types[0]
        )
        available_slot.reserve()
        return available_slot
