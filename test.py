from SYM import SYM
from NUM import NUM
from strings import oo
from utils import getThe, rand, rnd, setSeed

def settings_test():
    err = 0
    val = oo(getThe())
    if val != '{:dump false :go all :help false :seed 937162211}':
        err += 1
    return err

def rand_test():
    err = 0
    num1, num2 = NUM(), NUM()

    setSeed(getThe()['seed'])
    for i in range(1, 10**3):
        num1.add(rand(0, 1))
    
    setSeed(getThe()['seed'])
    for i in range(1, 10**3):
        num2.add(rand(0, 1))

    m1, m2 = rnd(num1.mid(), 10), rnd(num2.mid(), 10)

    if m1 != m2:
        err += 1
    if rnd(m1, 1) != 0.5:
        err += 1

    return err

def sym_test():
    err, sym = 0, SYM()
    for c in ["a","a","a","a","b","b","c"]:
        sym.add(c)
    
    if sym.mid() != "a":
        err += 1
    if sym.div() > (1.379 + 0.001) or sym.div() < (1.379 - 0.001):
        err += 1
    return err

def num_test():
    err, num = 0, NUM()
    for i in [1,1,1,1,2,2,3]:
        num.add(i)

    if num.mid() > (1.57142857 + 0.01) or num.mid() < (1.57142857 - 0.01):
        err += 1
    if rnd(num.div()) > (0.787 + 0.01) or rnd(num.div()) < (0.787 - 0.01):
        err += 1
    return err
