#!/usr/bin/env python

# This file is an example of multiple inheritance
# To view the code run the python interactive shell
#  enter the the following:
# >>> from flyingboat import *
# >>> seaDuck.FlyingBoat()
# >>> seaDuck.flyInTheAir()
# Output: Flying...
# >>> seaDuck.floatOnWater()
# Output: Floating...

class Airplane:
    """Airplane class for defining objects that are of the Airplane class"""
    def flyInTheAir(self):
        print('Flying...')
    
class Ship:
    """Ship class for defining objects that are of the Ship class; objects that float on the water"""
    def floatOnWater(self):
        print('Floating...')

class FlyingBoat(Airplane, Ship):
    """FlyingBoat class for defining objects that are of both the Airplane class and the Ship class"""
    pass