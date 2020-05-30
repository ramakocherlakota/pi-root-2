import BVMath
from BitVector import BitVector

x = BitVector(bitstring = "0001110000")
y = BitVector(bitstring = "01011001")

print(BVMath.subtract(x, y))
