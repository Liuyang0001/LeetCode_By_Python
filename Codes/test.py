import bisect
from collections import OrderedDict
from itertools import permutations
from typing import List

citations = [5, 4, 4, 3, 1]
l1 = [1, 2]
l2 = [1]
s = set(l2).__xor__(l1)
# print(dir(set))
print(s)
print(dir(OrderedDict))
dic = {1: (2,3), 2: (1,4), 1: (5,2)}
l = sorted(dic.items())
print(l)