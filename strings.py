from collections import OrderedDict

def fmt(sControl, *args):
    i, x, counter = 0, 0, 0
    rangeArr = range(len(sControl))
    
    while x < len(sControl):
        i = rangeArr[x]
        i2 = rangeArr[x+1]

        if sControl[i] == '%':
            if sControl[i2] == 'o':
                print(oct(args[counter]), end='')
                x += 1
            elif sControl[i2] == 'x':
                print(hex(args[counter]), end='')
                x += 1
            elif sControl[i2] == 'X':
                print(hex(args[counter]).upper(), end='')
                x += 1
            else:
                print(args[counter], end='')
                x += 1

            counter += 1
        else:
            print(sControl[i], end='')

        x += 1

def oo():
    pass

def o(t):
    pass

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1
    
    val = None

    try:
        val = int(s)
    except TypeError as te:
        val = fun(s.strip())
    except ValueError as ve:
        val = fun(s.strip())

    return val