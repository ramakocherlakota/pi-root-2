import sys
from math import sqrt

z = float(sys.argv[1])
count = int(sys.argv[2])
u = (1 + sqrt(4 * z + 1) ) / 2

u_k = 0
U = 1

for i in range(count):
    u_k = sqrt(z + u_k)
    U = U * u_k
    print(U, u_k, u, U / u ** i)
