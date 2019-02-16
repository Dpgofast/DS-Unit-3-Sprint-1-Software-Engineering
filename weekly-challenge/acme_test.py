#!/usr/bin/env python

import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, adjs, noun


class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are thetops!'''
    def test_default_product_price(self):
        '''Test default product price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        '''Test default product weight is 20'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        '''test stealability'''
        prod = Product('Golden Schoolbus', price=100)
        self.assertEqual(prod.stealability(), 'Very stealable!')

    def test_explosiveness(self):
        '''Test the Boom!'''
        prod = Product('C4', flammability=100.)
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    '''`test_default_num_products` which checks that it really does receive
    a list of length 30, and `test_legal_names` which checks that the
    generated names for a default batch of products are all valid possible
    names to generate (adjective, space, noun, from the lists of possible
    words)'''

    def test_default_num_products(self):
        '''check that it really does receive a list of
        length 30'''
        thangs = generate_products()
        self.assertEqual(len(thangs), 30)

    def test_legal_names(self):
        '''check that the generated names for a
        default batch of products are all valid possible names to generate
        (adjective, space, noun, from the lists of possible words)'''
        thangs = generate_products()
        names = [x.name for x in thangs]
        for name in names:
            self.assertEqual(len(name.split(' ')), 2)
        for name in names:
            named = name.split(' ')
            ads = named[0]
            nns = named[1]
            self.assertIn(ads, adjs)
            self.assertIn(nns, noun)

if __name__ == '__main__':
    unittest.main()
