# Author: Nathan
# This is an order object for the cafe menu application, contains various
# information about the order.

from typing import Dict
from typing import Union


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
        self.statuscode = 0
        self.status = 'Preparing'
        self.items = ''

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

    def set_courier(self, courier: Union[int, str]) -> bool:
        """Set order's courier index with input string or integer

        Args:
            courier (str): courier
        """
        if isinstance(courier, int):
            self.courier = courier
        elif isinstance(courier, str):
            if courier.strip() != '':
                self.courier = int(courier)
                return True
            else:
                return False
        else:
            return False

    def get_courier(self) -> Union[int, str]:
        """Returns the assigned courier index.

        Returns:
            str: The courier index, None if courier is blank.
        """
        if self.courier is not None:
            return self.courier
        else:
            return 'None'

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
                self.statuscode = 0
                self.status = 'Preparing'
            case '1':  # Awaiting pickup
                self.statuscode = 1
                self.status = 'Awaiting pickup'
            case '2':  # Out for delivery
                self.statuscode = 2
                self.status = 'Out for delivery'
            case '3':  # Delivered
                self.statuscode = 3
                self.status = 'Delivered'
            case _:  # Invalid input
                print('Invalid update status entered, status unchanged.')
                return False
        return True

    def set_items(self, item_string: str):
        """Set order's products from input string.

        Args:
            item_string (str): Concatenated string of products assigned to
            order.
        """
        if item_string != '':
            self.items = item_string
        else:
            return

    def get_items(self) -> str:
        """Returns the item indices as a comma-seperated string.

        Returns:
            str: The item indices as a comma-seperated string.
        """
        if self.items != '':
            return self.items
        else:
            return 'None'

    def get_order(self) -> Dict:
        """Returns the order as a dictionary.

        Returns:
            Dict: The order.
        """
        return {'customer_name': self.customer_name,
                'customer_address': self.customer_address,
                'customer_phone': self.customer_phone,
                'courier': self.courier,
                'status': self.status,
                'items': self.items}
