import math

the = {}
o_file = None

Seed=937162211
def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def setSeed(val):
  global Seed
  Seed = val

def rand(lo, hi):
  global Seed
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces=3):
  return round(n, nPlaces)

def getThe():
  global the 
  return the

def setThe(options):
  global the
  the = options

def get_ofile():
  global o_file
  if o_file is None:
    o_file = open('etc/out', 'w', encoding='utf-8')
    
  return o_file
