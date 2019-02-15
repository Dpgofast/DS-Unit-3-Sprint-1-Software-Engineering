 #!/usr/bin/env python
 
import unittest
from acme import Product, BoxingGlove

class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are thetops!'''
    def test_default_product_price(self):
        '''Test default product price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price,10)
    def test_default_weight(self):
        '''Test default product weight is 20'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight,20)
    def test_stealability(self):
        '''test stealability'''
        prod = Product('Golden Schoolbus',price=1000, weight=1)
        self.assertEqual(prod.stealability(),'Very stealable!')
    def test_explosiveness(self):
        '''Test the Boom!'''
        prod = Product('C4',flamability=100)
        self.assertEqual(prod.explode(),'...BABOOM!')