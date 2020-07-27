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
    
    n = int(input())
    a = list(map(int, input().split()))
    max_num = sum(a)
 
    for i in range(n):
        
        while(a[i]%3 == 2 or a[i]%2 == 0):
            a[i] -= 1
 
    print(max_num - sum(a))
    

if __name__ == '__main__':
	main()
