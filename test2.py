import sys
import BVMath
from BitVector import BitVector

sz = int(sys.argv[1])
count = int(sys.argv[2])

two = BitVector(intVal=2, size=2)
two.pad_from_right(sz-2)
current = BVMath.sqrt(two)

for i in range(count):
    current[0] = 1
    print("current=",current)
    current = BVMath.sqrt(current)
    print("sqrt(current)=",current)
