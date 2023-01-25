from collections import OrderedDict

def map(t, fun, temp):
    temp = OrderedDict()
    for k, v in enumerate(t):
        v, k = fun(v)
        if k is None:
            temp[1+len(temp.keys)] = v
        else:
            temp[k] = v
    return temp

def kap(t, fun, temp):
    temp = OrderedDict()
    for k, v in enumerate(t):
        v, k = fun(k, v)
        if k is None:
            temp[1+len(temp.keys)] = v
        else:
            temp[k] = v
    return temp

def sort(t):
    t.sort()
    return t

def keys(t):
    ks = t.keys()
    ks.sort()
    return ks