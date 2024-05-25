import sys
import BitVector
import SqrtState

x = int(sys.argv[1])

ss = SqrtState.SqrtState(BitVector.BitVector(intVal=1, size=1),
                         BitVector.BitVector(intVal=0, size=1000),
                         BitVector.BitVector(intVal=1, size=1))

for i in range(x):
    print(ss)
    print(int(ss.root) / (2 ** (ss.root.length()-1)))
    ss.step()
