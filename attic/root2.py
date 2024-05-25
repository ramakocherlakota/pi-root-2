from BitVector import BitVector

r = 0.414213562373095

bv = BitVector(size=2, intVal=1)
for i in range(1, 30):
    print(i)
    if r > 2 ** (-i):
        r -= 2 ** (-i)
        bv += BitVector(size=1, intVal=1)
    else:
        bv += BitVector(size=1, intVal=0)

print(bv)
