import BitVector

class SqrtState :
    bit0 = BitVector.BitVector(intVal=0, size=1)
    bit1 = BitVector.BitVector(intVal=1, size=1)
    bit00 = BitVector.BitVector(intVal=0, size=2)
    bit01 = BitVector.BitVector(intVal=1, size=2)

    tail = BitVector.BitVector(size=0)
    root = BitVector.BitVector(size=0)
    delta = BitVector.BitVector(size=0)
    

    def __init__(self, root, tail, delta):
        self.root = root
        self.tail = tail
        self.delta = delta

    def __str__(self):
        return "root = {}, tail={}, diff={}".format(str(self.root), str(self.tail), str(self.delta))

    def step(self):
        d = self.delta[self.delta.next_set_bit():]
        down = d + self.tail[-2:]
        self.tail = self.tail[:-2]
        left = self.root + self.bit00
        if left < down:
            self.delta = self.subtract(down, self.root + self.bit01)
            self.root += self.bit1
        else:
            self.delta = down
            self.root += self.bit0

    def increment(self, bv):
        revcomp = ~bv.reverse()
        first_one = revcomp.next_set_bit(0)
        if first_one == bv.length():
            # revcomp is all zeros, which means bv is all ones, return 100..0
            return self.bit1 + revcomp
        else:
            # in bv, everything to the right of -first_one is 1
            # set them all to zero and set -first_one to 1
            leftpart = (bv[:bv.length()-first_one-1] + self.bit1)
            leftpart.pad_from_right(bv.length() - leftpart.length())
            return leftpart

    def subtract(self, big, little):
        little.pad_from_left(big.length() - little.length())
        len = big.length()
        comp = self.increment(~little)
        return self.add(big, comp)[1:]

    def add(self, x, y):
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
                revsum += self.bit0
            else:
                revsum += self.bit1
        if c == 1:
            revsum += self.bit1
        return revsum.reverse()
                
            
        

