import sys
from math import sqrt

x = float(sys.argv[1])
count = int(sys.argv[2])
u = 0
lim = (1 + sqrt(1 + 4 * x)) / 2
factor = 2 * lim
prod = 1

for n in range(count) :
    u = sqrt(x + u)
    prod = factor * prod
    delta = lim - u
    print(delta * prod)


