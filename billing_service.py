from interfaces.billing_service import BillingService
from datetime import datetime


class Biller(BillingService):

    @staticmethod
    def get_charges(parking_ticket):
        total_duration = datetime.now() - parking_ticket.get_start_time()
        total_duration_in_hours = total_duration.total_seconds() // 60 // 60

        parking_rates = parking_ticket.get_rates()
        return max(
            parking_rates["minimum_charge"],
            parking_rates["hourly_charge"] * total_duration_in_hours,
        )
