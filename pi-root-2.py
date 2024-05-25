import sys
from math import sqrt

n = int(sys.argv[1])
a_i = sqrt(2.0)
factor = 4

for i in range(n):
    pi = factor * (sqrt(2.0 - a_i))
    Pi = 2 * pi / (1 + a_i * a_i / 4)
    print(f"{i+2} {pi} {Pi}")
    a_i = sqrt(2.0 + a_i)
    factor = 2 * factor
