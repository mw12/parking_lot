from any_fit_parking_spot_service import AnyFitParkingSpotService
from best_fit_parking_spot_service import BestFitParkingSpotService
from enums import SlotReservationStrategy
from parking_slot import ParkingSlot


class SlotManagerFactory:
    def create_slot_manager(type):
        if not isinstance(type, SlotReservationStrategy):
            raise ValueError()
        if type == SlotReservationStrategy.MATCH_ONLY:
            return BestFitParkingSpotService(ParkingSlot)
        elif type == SlotReservationStrategy.MATCH_PLUS:
            return AnyFitParkingSpotService(ParkingSlot)
        else:
            raise NotImplementedError()
