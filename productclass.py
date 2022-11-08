# Author: Nathan
# This is an product object for the cafe menu application, contains various
# information about the product.

from typing import Dict


class Product:

    def __init__(self, name: str, price: float) -> None:
        """Initialise product.

        Args:
            name (str): Initial product name.
            price (float): Initial product price.
        """
        self.name = name
        self.price = price

    def set_product_name(self, name: str) -> None:
        """Set product's name with input string.

        Args:
            name (str): The replacement product name.
        """
        self.name = name

    def set_product_price(self, price: float) -> None:
        """Set product's price with input float.

        Args:
            price (float): The replacement product price.
        """
        self.price = price

    def get_product_price(self) -> str:
        """Return the product price formatted as GBP.

        Returns:
            str: The currency.
        """
        return '£{:,.2f}'.format(self.price)

    def get_product(self) -> Dict:
        """Returns the product as a dictionary.

        Returns:
            Dict: The product.
        """
        return vars(self)
