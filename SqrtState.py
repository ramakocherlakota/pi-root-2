import BVMath

class SqrtState :

    def __init__(self, root, tail, delta):
        self.root = root
        self.tail = tail
        self.delta = delta

    def __str__(self):
        return "root = {}, tail={}, delta={}".format(str(self.root), str(self.tail), str(self.delta))

    def step(self):
#        d = self.delta[self.delta.next_set_bit():]
#        print(" changed ", self.delta, " to ", d)
        d = self.delta
        down = d + self.tail[:2]
        self.tail = self.tail[2:]
        left = self.root + BVMath.bit01()
#         print("left=",left, " down=", down, left <= down)
        if left <= down:
            self.delta = BVMath.subtract(down, self.root + BVMath.bit01())
            self.root += BVMath.bit1()
        else:
            self.delta = down
            self.root += BVMath.bit0()

                
            
        

