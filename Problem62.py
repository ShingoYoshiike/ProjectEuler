# ProjectEuler
# Problem62
from itertools import *

def isSame(n, m):
  l1 = list(str(n))
  l2 = list(str(m))
  l1.sort()
  l2.sort()
  return l1 == l2

CubeList = [n**3 for n in range(385, 1000)]
