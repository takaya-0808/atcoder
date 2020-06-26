import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush
from math import ceil, floor, sqrt, gcd
from copy import deepcopy
from decimal import *

def main():
    a,b = map(Decimal, input().split())
    result = a*b
    print(int(result))
    
if __name__ == "__main__":
    main()