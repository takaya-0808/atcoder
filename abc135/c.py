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
    num = int(input())        
    a_list = list(map(int, input().split()))
    a = sum(a_list)
    b_list = list(map(int, input().split()))

    for i in range(num):
        if a_list[i] >= b_list[i]:
            a_list[i] -= b_list[i]
            b_list[i] = 0
        else:
            b_list[i] -= a_list[i]
            a_list[i] = 0
            if a_list[i+1] >= b_list[i]:
                a_list[i+1] -= b_list[i]
            else:
                a_list[i+1] = 0
        

    print(a - sum(a_list))


if __name__ == "__main__":
    main()