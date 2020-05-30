form BitVector import BitVector

class BV :
    _bv = None

    def __init__(bv):
        _bv = bv

    def quick_bv(self, ival, sz):
        return BV(BitVector(intVal=ival, size=sz))

    def bit0(self):
        return self.quick_bv(0, 1)

    def bit1(self):
        return self.quick_bv(1, 1)

    def bit00(self):
        return self.quick_bv(0, 2)

    def bit01(self):
        return self.quick_bv(1, 2)

    def increment(self):
        bv = self._bv
        revcomp = ~bv.reverse()
        first_one = revcomp.next_set_bit(0)
        if first_one == bv.length():
            # revcomp is all zeros, which means self is all ones, return 100..0
            return self.bit1() + revcomp
        else:
            # in self, everything to the right of -first_one is 1
            # set them all to zero and set -first_one to 1
            leftpart = (self[:self.length()-first_one-1] + self.bit1())
            leftpart.pad_from_right(self.length() - leftpart.length())
            return leftpart

    def subtract(self, other):
        self.pad_from_left(self.length() - other.length())
        len = self.length()
        comp = (~other).increment()
        return self.add(comp)[1:]

    def add(x, y):
        if x.length() > y.length():
            y.pad_from_left(x.length() - y.length())
        else:
            x.pad_from_left(y.length() - x.length())
            revsum = BitVector.BitVector(size=0)
            c = 0 # carry flag
            n = x.length()
        for i in range(x.length()):
            s = x[n-i-1] + y[n-i-1] + c
            if s > 1:
                c = 1
            else:
                c = 0
            if s % 2 == 0:
                revsum += x.bit0()
            else:
                revsum += x.bit1()
        if c == 1:
            revsum += x.bit1()
        return revsum.reverse()
    
        
