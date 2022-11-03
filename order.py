# Author: Nathan
# This is an order object for the cafe menu application, contains various
# information about the order.

from typing import Dict


class Order:
    """Class used for storing order attributes."""
    def __init__(self, name: str, address: str, phone: str) -> None:
        """Initialise order.

        Args:
            name (str): Initial customer name.
            address (str): Initial customer address.
            phone (str): Initial customer phone number.
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.status = 'Preparing'

    def set_order_name(self, name: str) -> None:
        """Set customer's name with input string

        Args:
            name (str): The replacement customer name.
        """
        self.name = name

    def set_order_address(self, address: str) -> None:
        """Set customer's address with input string

        Args:
            address (str): The replacement customer address.
        """
        self.address = address

    def set_order_phone(self, phone: str) -> None:
        """Set customer's phone with input string

        Args:
            phone (str): The replacement customer phone number.
        """
        self.phone = phone

    def set_order_status(self, index: str) -> bool:
        """Set order's status from a list of options.

        Args:
            index (str): The index for the replacement status.

        Returns:
            bool: True if function successful, False if not.
        """
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
        """Returns the order as a dictionary.

        Returns:
            Dict: The order.
        """
        return {'customer_name': self.name,
                'customer_address': self.address,
                'customer_phone': self.phone,
                'status': self.status}
