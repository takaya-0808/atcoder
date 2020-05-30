import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy

def main():
    l,r = map(int, input().split())
    ans = 2019

    if r - l >= 2019:
        print(0)
        sys.exit()

    for i in range(l,r+1):
        for j in range(i+1,r+1):
            if i%2019 == 0 or j%2019 == 0:
                ans = 0
                break
            else:
                ans = min(ans, (i*j)%2019)
    print(ans)
   
if __name__ == "__main__":
    main()