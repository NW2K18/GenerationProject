# Author: Nathan
# This is an order object for the cafe menu application, contains various
# information about the order.

from typing import Dict


class Order:
    def __init__(self, name, address, phone) -> None:
        self._name = name
        self._address = address
        self._phone = phone
        self._status = 'Preparing'


    # Set customer's name with input string
    def set_order_name(self, name) -> None:
        pass

    
    # Set customer's address with input string
    def set_order_address(self, address) -> None:
        pass


    # Set customer's phone with input string
    def set_order_phone(self, phone) -> None:
        pass


    # Set order's status from a list of options.
    def set_order_status(self, index) -> None:
        pass


    def get_order(self) -> Dict:
        return {'customer_name' : self._name,
                'customer_address' : self._address,
                'customer_phone' : self._phone,
                'status' : self._status}
