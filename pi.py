from __future__ import print_function
from __future__ import division
import random, math
from decimal import Decimal

noInside = 0
n = 0

while True:
    n += 1
    if (random.random() ** 2 + random.random() ** 2) ** 0.5 < 1.0:
        noInside += 1
    print((Decimal(noInside) / Decimal(n)) * 4, " after " + str(n) +" iterations")
