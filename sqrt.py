# https://engineering.purdue.edu/kak/dist/BitVector-3.4.9.html
import BitVector
import sys

digits = int(sys.argv[1])

two = BitVector.BitVector(intVal=2, size=2 * digits)
two << (2 * digits - 2)





def extract_first_two(bv):
    return (bv[0:2], bv[2:])

def sqrt(bv) :
    if bv.size() % 2 != 0:
        raise("Must be an even length BitVector")
    (next2, rest) = extract_first_two(bv)
    root = BitVector.BitVector(size=1)
    if start[0] == 1 or start[1] == 1:
        root[0] = bit1
    else:
        root[0] = bit0
    left = root + bit0
    rem = subtract(




