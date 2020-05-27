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
    n,d = map(int, input().split())
    list_num = []
    for i in range(n):
        list_x = list(map(int, input().split()))
        list_num.append(list_x)
    
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                ans = 0
                result_num = 0
                for l in range(d):
                    result_num += pow(abs(list_num[i][l] - list_num[j][l]),2)
                ans = sqrt(result_num)
                
                if ans.is_integer():
                    count += 1
    print(count)

if __name__ == "__main__":
    main()