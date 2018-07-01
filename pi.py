import random, math
from decimal import Decimal
noInside = 0
for n in range(1, 10000000):
    if (random.random() ** 2 + random.random() ** 2) ** 0.5 < 1.0:
        noInside += 1
    print((Decimal(noInside) / Decimal(n)) * 4, " after " + str(n) +" iterations")
