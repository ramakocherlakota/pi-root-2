import math

c = math.sqrt(2) / 2
s = math.sqrt(2) / 2
n = 2

for i in range(20):
    p = 2**n * s * c
    P = 2**n * s / c
    print("{}\t{}\t{}\t{}\t{}\t{}".format(n, 2**n, p, P, s, c))
    n = n+1
    s = math.sqrt((1 - c) / 2)
    c = math.sqrt((1 + c) / 2)
             
