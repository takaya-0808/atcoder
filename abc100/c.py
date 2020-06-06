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
    num = int(input())
    x_list = list(map(int, input().split()))
    ans = 0

    for i in range(num):
        x = x_list[i]
        while  x%2 == 0:
            ans += 1
            x = x//2

    print(ans)

    
if __name__ == '__main__':
    main()