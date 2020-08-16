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
    s = input()   
    count = 0
    ans = 0
    for i in s:
        if i == "R":
            count += 1
            ans = count
        else:
            count = 0
    print(ans)

if __name__ == '__main__':
	main()
