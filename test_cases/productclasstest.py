# Author: Nathan
# Unit tests for productclass.py

import unittest

import productclass


class TestProductAttributes(unittest.TestCase):
    def test_create_product(self):
        test_product = productclass.Product('Water', 0.75)
        self.assertEqual(test_product.name, 'Water')
        self.assertEqual(test_product.price, 0.75)

    def test_set_attributes(self):
        test_product = productclass.Product('Water', 0.75)

        test_product.set_product_name('Pepsi')
        test_product.set_product_price(2.25)

        self.assertEqual(test_product.name, 'Pepsi')
        self.assertEqual(test_product.price, 2.25)

    def test_get_product_price(self):
        test_product = productclass.Product('Water', 0.75)
        self.assertEqual(test_product.get_product_price(), '£0.75')

        test_product.set_product_price(1.45)
        self.assertEqual(test_product.get_product_price(), '£1.45')
        test_product.set_product_price(1.4)
        self.assertEqual(test_product.get_product_price(), '£1.40')
        test_product.set_product_price(1)
        self.assertEqual(test_product.get_product_price(), '£1.00')
        test_product.set_product_price(0)
        self.assertEqual(test_product.get_product_price(), '£0.00')

        test_product.set_product_price(1.457)
        self.assertEqual(test_product.get_product_price(), '£1.46')
        test_product.set_product_price(1.454)
        self.assertEqual(test_product.get_product_price(), '£1.45')

    def test_get_product(self):
        test_product = productclass.Product('Water', 0.75)
        self.assertEqual(test_product.get_product(),
                         {'name': 'Water',
                         'price': 0.75})


if __name__ == '__main__':
    unittest.main()
