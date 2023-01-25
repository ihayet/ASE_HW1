from VAL import VAL
import math

class NUM(VAL):
    total, mu, m2, lo, hi = 0, 0, 0, 0, 0

    def __init__(self):
        self.total, self.mu, self.m2 = 0, 0, 0
        self.lo, self.hi = -math.inf, math.inf

    def add(self, x):
        if self.total != "?":
            self.total += 1
            temp = x - self.mu
            self.mu += temp/self.total
            self.m2 += temp*(x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if (self.m2 < 0 or self.total < 2) else (self.m2/(self.total-1))**0.5
