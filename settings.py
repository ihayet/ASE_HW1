from collections import OrderedDict
import re

def settings(s):
    t = OrderedDict()
    res = re.search(r'\n[%s]+[-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)', s)
    t[res.group(1)] = res.group(2)

