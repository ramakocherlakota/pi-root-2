import BVMath
import sys
from BitVector import BitVector

of = sys.argv[1]
pad = sys.argv[2]

x = BitVector(bitstring = of)
x.pad_from_right(int(pad))
print(x)
print(BVMath.sqrt(x))
