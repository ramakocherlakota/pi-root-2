import sys
import BVMath
from BitVector import BitVector

sz = int(sys.argv[1])
count = int(sys.argv[2])

two = BitVector(intVal=2, size=2)
two.pad_from_right(sz-2)
plus = BVMath.sqrt(two)

for i in range(count):
    # add 2
    plus[0] = 1
    plus = BVMath.sqrt(plus)
    # subtract from 2
    minus = ~plus
    # shift over by i
    minus[0] = 0
    print(minus.shift_left(2*i + 4))
    
