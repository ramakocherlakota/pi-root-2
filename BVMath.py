from BitVector import BitVector
import SqrtState

def quick_bv(ival, sz) :
    return BitVector(intVal=ival, size=sz)

def bit0():
    return quick_bv(0, 1)

def bit1():
    return quick_bv(1, 1)

def bit00():
    return quick_bv(0, 2)

def bit01():
    return quick_bv(1, 2)

def plus1(bv):
    revcomp = ~bv.reverse()
    first_one = revcomp.next_set_bit(0)
    if first_one == bv.length():
        # revcomp is all zeros, which means self is all ones, return 100..0
        return bit1() + revcomp
    else:
        # in self, everything to the right of -first_one is 1
        # set them all to zero and set -first_one to 1
        leftpart = (bv[:bv.length()-first_one-1] + bit1())
        leftpart.pad_from_right(bv.length() - leftpart.length())
        return leftpart

def trim(x):
    t = x[x.next_set_bit(0):]
    return t;

def subtract(x, y):
    if x < y:
        raise(Exception("can't subtract these numbers, you'd end up below zero"))
    x = trim(x)
    y = trim(y)

    if x.length() < y.length():
        x.pad_from_left(x.length() - y.length())
    else:
        y.pad_from_left(y.length() - x.length())
          
    comp = plus1(~y)
    diff = add(x, comp)[1:]
    return diff

def add(x, y):
    if x.length() > y.length():
        y.pad_from_left(x.length() - y.length())
    else:
        x.pad_from_left(y.length() - x.length())
    revsum = BitVector(size=0)
    c = 0 # carry flag
    n = x.length()
    for i in range(x.length()):
        s = x[n-i-1] + y[n-i-1] + c
        if s > 1:
            c = 1
        else:
            c = 0
        if s % 2 == 0:
            revsum += bit0()
        else:
            revsum += bit1()
    if c == 1:
        revsum += bit1()
    return revsum.reverse()

def sqrt(bv) :
    shift = 0
    while bv[:2] == bit00() and bv.length() > 1:
        bv = bv[2:]
        shift += 1
    tail = bv[2:]
    root = bit01()
    delta = subtract(bv[:2], bit01())
    state = SqrtState.SqrtState(root, tail, delta)
    while state.tail.length() > 1:
#         print(state)
        state.step()
    return(state.root.shift_right(shift))

    
