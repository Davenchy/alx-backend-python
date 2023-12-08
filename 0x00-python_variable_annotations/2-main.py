#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

and = floor(3.14)

print(and == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format( and , type( and )))
