import math

Seed=937162211
def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi):
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces=3):
  return round(n, nPlaces)