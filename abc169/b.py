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
    n = int(input())
    a_list = tuple(map(int, input().split()))
    num = 1e18
    ans = 1
    if (0 in a_list):
        print(0)
        sys.exit()
    for i in range(n):
        ans *= a_list[i]
        if ans > num:
            print(-1)
            sys.exit()

    
    if ans <= num:
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()