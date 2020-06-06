import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt, gcd
from copy import deepcopy

def main():
    d,n = map(int, input().split())
    if n == 100:
        print((100**d) * (n+1)) 
    else:
        print((100**d) * n)  
if __name__ == '__main__':
    main()