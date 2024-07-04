from interfaces.parking_spot_service import SpotServiceInterface
from constants import VehicleTypeParkingSlotTypeMatch


class BestFitParkingSpotService(SpotServiceInterface):

    def __init__(self, parking_slot_data_manager):
        self.parking_slot_data_manager = parking_slot_data_manager

    def reserve_available_slot(self, vehicle):
        best_fit_slot_type = VehicleTypeParkingSlotTypeMatch.get_fitting_slot_type(
            vehicle.get_type()
        )
        available_slot = self.parking_slot_data_manager.get_best_available_slot(
            best_fit_slot_type
        )
        available_slot.reserve()
        return available_slot
