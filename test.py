from SYM import SYM
from NUM import NUM
from utils import rnd

def sym_test(type):
    err = 0
    if type == "sym":
        sym = SYM()
        for c in ["a","a","a","a","b","b","c"]:
            sym.add(c)
        
        if sym.mid() != "a":
            err += 1
        if sym.div() > (1.379 + 0.001) or sym.div() < (1.379 - 0.001):
            err += 1
    return err

def num_test(type):
    err = 0
    if type == "num":
        num = NUM()
        for i in [1,1,1,1,2,2,3]:
            num.add(i)

        print(num.mid())
        print(num.div())
        
        if num.mid() > (1.57142857 + 0.01) or num.mid() < (1.57142857 - 0.01):
            err += 1
        if rnd(num.div()) > (0.787 + 0.01) or rnd(num.div()) < (0.787 - 0.01):
            err += 1
    return err

def test(type, msg, fun):
    return fun(type)

print(test("sym", "test", sym_test))
print(test("num", "test", num_test))
