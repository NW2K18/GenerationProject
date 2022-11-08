# Author: Nathan
# This is an order object for the cafe menu application, contains various
# information about the order.

from typing import Dict, List


class Order:
    """Class used for storing order attributes."""
    def __init__(self, name: str, address: str, phone: str) -> None:
        """Initialise order.

        Args:
            name (str): Initial customer name.
            address (str): Initial customer address.
            phone (str): Initial customer phone number.
        """
        self.customer_name = name
        self.customer_address = address
        self.customer_phone = phone
        self.courier = None
        self.status = 'Preparing'
        self.items = []

    def set_order_name(self, name: str) -> None:
        """Set customer's name with input string.

        Args:
            name (str): The replacement customer name.
        """
        self.customer_name = name

    def set_order_address(self, address: str) -> None:
        """Set customer's address with input string.

        Args:
            address (str): The replacement customer address.
        """
        self.customer_address = address

    def set_order_phone(self, phone: str) -> None:
        """Set customer's phone with input string.

        Args:
            phone (str): The replacement customer phone number.
        """
        self.customer_phone = phone

    def set_courier(self, courier: str) -> None:
        """Set order's courier index with input string

        Args:
            courier (str): courier
        """
        self.courier = courier

    def set_order_status(self, option: str) -> bool:
        """Set order's status from a list of options.
        0 = Preparing
        1 = Awaiting pickup
        2 = Out for delivery
        3 = Delivered

        Args:
            option (str): The index for the replacement status.

        Returns:
            bool: True if function successful, False if not.
        """
        match option:
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

    def set_items(self, items: List):
        """Set order's products from input List.

        Args:
            items (List): List of products assigned to order.
        """
        for item in items:
            self.items.append(item)

    def get_order(self) -> Dict:
        """Returns the order as a dictionary.

        Returns:
            Dict: The order.
        """
        return vars(self)
