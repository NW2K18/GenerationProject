# Author: Nathan
# Unit tests for productclass.py

import unittest

import productclass as productclass


class TestProductClass(unittest.TestCase):

    def setUp(self) -> None:
        self.test_product = productclass.Product('Water', 0.75)

    def test_create_product(self):
        self.assertEqual(self.test_product.name, 'Water')
        self.assertEqual(self.test_product.price, 0.75)

    def test_set_attributes(self):
        self.test_product.set_product_name('Pepsi')
        self.test_product.set_product_price(2.25)

        self.assertEqual(self.test_product.name, 'Pepsi')
        self.assertEqual(self.test_product.price, 2.25)

    def test_get_product_price(self):
        self.assertEqual(self.test_product.get_product_price(), '£0.75')

        self.test_product.set_product_price(1.45)
        self.assertEqual(self.test_product.get_product_price(), '£1.45')
        self.test_product.set_product_price(1.4)
        self.assertEqual(self.test_product.get_product_price(), '£1.40')
        self.test_product.set_product_price(1)
        self.assertEqual(self.test_product.get_product_price(), '£1.00')
        self.test_product.set_product_price(0)
        self.assertEqual(self.test_product.get_product_price(), '£0.00')

        self.test_product.set_product_price(1.457)
        self.assertEqual(self.test_product.get_product_price(), '£1.46')
        self.test_product.set_product_price(1.454)
        self.assertEqual(self.test_product.get_product_price(), '£1.45')

    def test_get_product(self):
        self.assertEqual(self.test_product.get_product(),
                         {'name': 'Water',
                         'price': 0.75})


if __name__ == '__main__':
    unittest.main()
