from VAL import VAL
import math

class SYM(VAL):
    total, most, mode = 0, 0, None
    sym_counter = {}

    def __init__(self):
        self.total, self.most, self.mode = 0, 0, None
        self.sym_counter = {}

    def add(self, x):
        if x != "?":
            self.total += 1

            if x in self.sym_counter:
                self.sym_counter[x] += 1
            else:
                self.sym_counter[x] = 1

            if self.sym_counter[x] > self.most:
                self.most = self.sym_counter[x]
                self.mode = x

    def mid(self):
        return self.mode

    def div(self):
        def ent(p):
            return p*math.log(p, 2)

        e = 0
        for sym in self.sym_counter:
            e += ent(self.sym_counter[sym]/self.total)

        return -e