# Author: Nathan
# This is an courier object for the cafe menu application, contains various
# information about the courier.

from typing import Dict, Union


class Courier:

    def __init__(self, name: str, phone: str) -> None:
        """Initialise courier.

        Args:
            name (str): Initial courier name.
            phone (str): Initial courier phone number.
        """
        self.name = name
        self.phone = phone

    def set_courier_name(self, name: str) -> None:
        """Set courier's name with input string.

        Args:
            name (str): The replacement courier name.
        """
        self.name = name

    def set_courier_phone(self, phone: str) -> None:
        """Set product's phone number with input string.

        Args:
            phone (str): The replacement product price.
        """
        self.phone = phone

    def get_courier(self) -> Dict:
        """Returns the courier as a dictionary.

        Returns:
            Dict: The courier.
        """
        return vars(self)
