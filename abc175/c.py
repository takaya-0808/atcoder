import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt
from copy import deepcopy


def main():
    x,k,d = map(int, input().split())

    if abs(x) <= d*k:
        s = x//d
        a = x%d
        if (k-s) % 2 == 0:
            print(a)
        else:
            if abs(a + d) <= abs(a - d):
                print(abs(a+d))
            else:
                print(abs(a - d))
    else:
        print(abs(x) - d*k)

if __name__ == '__main__':
	main()
