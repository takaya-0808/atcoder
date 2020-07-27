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
    
    txa, tya, txb, tyb, t, v = map(int, input().split())
    n = int(input())
    flag = False

    for i in range(n):
        b = list(map(int, input().split()))
        h =  sqrt((txa - b[0])**2 + (tya - b[1])**2) + sqrt((txb - b[0])**2 + (tyb - b[1])**2)
        if h <= t*v:
            flag = True
            break


    if flag:
        print("YES")
    else:
        print("NO")
    

if __name__ == '__main__':
	main()
