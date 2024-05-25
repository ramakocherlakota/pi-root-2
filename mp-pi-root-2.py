import sys
from mpmath import *
mp.pretty = True
mp.dps = 50

n = int(sys.argv[1])
a_i = sqrt(mp.mpf(2.0))
factor = mp.mpf(4.0)

for i in range(n):
    pi = factor * (sqrt(2.0 - a_i))
    Pi = 2 * pi / (1 + a_i * a_i / 4)
    print(f"{i+2} {pi} {Pi} {mp.pi - pi} {Pi - mp.pi}")
    a_i = sqrt(2.0 + a_i)
    factor = 2 * factor

