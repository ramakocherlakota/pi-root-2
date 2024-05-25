import sys
from math import sqrt

z = float(sys.argv[1])
count = int(sys.argv[2])
x = sqrt(z)
y = (1 + sqrt(4 * z + 1) ) / 2
prev = x

for i in range(count) :
    print(y, " ", x, " ", y-x, " ", prev / (y - x))
    prev = y - x
    x = sqrt(z + x)

