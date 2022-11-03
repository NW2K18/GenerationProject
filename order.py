# Author: Nathan
# This is an order object for the cafe menu application, contains various
# information about the order.

from typing import Dict


class Order:
    def __init__(self, name, address, phone) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.status = 'Preparing'

    # Set customer's name with input string
    def set_order_name(self, name) -> None:
        self.name = name

    # Set customer's address with input string
    def set_order_address(self, address) -> None:
        self.address = address

    # Set customer's phone with input string
    def set_order_phone(self, phone) -> None:
        self.phone = phone

    # Set order's status from a list of options.
    def set_order_status(self, index: str) -> bool:
        match index:
            case '0':  # Preparing
                self.status = 'Preparing'
            case '1':  # Awaiting pickup
                self.status = 'Awaiting pickup'
            case '2':  # Out for delivery
                self.status = 'Out for delivery'
            case '3':  # Delivered
                self.status = 'Delivered'
            case _:  # Invalid input
                print('Invalid update status entered, status unchanged.')
                return False
        return True

    def get_order(self) -> Dict:
        return {'customer_name': self.name,
                'customer_address': self.address,
                'customer_phone': self.phone,
                'status': self.status}
