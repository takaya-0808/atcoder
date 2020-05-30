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
    n = int(input())
    p_list = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i+1 != p_list[i]:
            count += 1
    
    if count >= 3:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()