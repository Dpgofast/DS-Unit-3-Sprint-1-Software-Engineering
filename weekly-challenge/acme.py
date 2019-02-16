#!/usr/bin/env python


class Product(object):
    '''All things related to acme business shall go through here,
    -  `name` (string with no default)
    - `price` (integer with default value 10)
    - `weight` (integer with default value 20)
    - `flammability` (float with default value 0.5)
    - `identifier` (integer, automatically genererated as a random (uniform)
    number anywhere from 1000000 to 9999999, includisve)(inclusive).'''

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        assert isinstance(price, int)
        assert isinstance(weight, int)
        assert isinstance(flammability, float)
        from random import randint
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ''' `stealability(self)` - calculates the price divided by the weight,
         and then returns a message: if the ratio is less than 0.5 return
         "Not so stealable...",if it is greater or equal to 0.5 but less than
         1.0 return "Kinda stealable.",and otherwise return "Very stealable!"
         '''
        yoink = (self.price / self.weight)
        if yoink >= 1:
            return 'Very stealable!'
        if yoink <= 1 or yoink == 0.5:
            return 'Kinda stealable.'
        if yoink <= 0.4 or yoink == 0:
            return 'Not so stealable.'

    def explode(self):
        '''calculates the flammability times the weight, and then
         returns a message: if the product is less than 10 return
         "...fizzle.",if it is greater or equal to 10 but less than 50 return
          "...boom!", and otherwise return "...BABOOM!!"'''

        blast = self.flammability * self.weight
        if blast <= 9:
            return '...fizzle.'
        if blast == 10 or blast <= 49:
            return '...boom!'
        if blast >= 50:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''Change the default `weight` to 10 (but leave other defaults unchanged)
        - Override the `explode` method to always return "...it's a glove."
        - Add a `punch` method that returns "That tickles." if the weight is
         below 5,"Hey that hurt!" if the weight is greater or equal to 5 but
         less than 15, and "OUCH!" otherwise'''

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        from random import randint
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def punch(self):
        if self.weight <= 4:
            return 'That Tickles.'
        if self.weight >= 5 or self.weight == 14:
            return 'Hey that hurt!'
        if self.weight >= 15:
            return 'OUCH!'

    def explode(self):
        return "...it's a glove."
