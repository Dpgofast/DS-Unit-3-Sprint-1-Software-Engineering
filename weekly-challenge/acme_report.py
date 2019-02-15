#!usr/bin/env python
adjs= ['Awesome','Shiny','Impressive','Portable','Improved']
noun= ['Anvil','Catapult','Disguise','Mousetrap', '???']


def generate_products(n=30):
    '''`generate_products()` should generate a given number of products (default
    30), randomly, and return them as a list'''
    from random import random, randint, choice 
    from acme import Product
    
    tings = []

    for l in range(n):
        name  = choice(adjs)+''+choice(noun)
        price = randint(5,100)
        weight= randint(5,100)
        flamability=random()*2.5
        stuff = Product(name,price,weight,flamability)
        tings.append(stuff)

def inventory_report(tings):
    '''`inventory_report()` takes a list of products, and prints a "nice" summary'''
    u_names = len(set([x.name for x in tings]))
    def mean (l):
        return sum(l)/len(l)
    m_price = mean([x.price for x in tings])
    m_weights= mean([x.weights for x in tings])
    m_flam = mean([x.flamability for x in tings])

if __name__ == '__main__':
    inventory_report(generate_products())