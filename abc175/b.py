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
    alist = list(map(int, input().split()))
    if n < 3:
        print(0)
        sys.exit()

    s = list(combinations(alist, 3))
    print(s)
    count = 0

    for i in s:
        if not(has_duplicates(i)):
            if i[0]+i[1]>i[2] and i[1]+i[2]>i[0] and i[2]+i[0]>i[1]:
                count += 1

    print(count)

def has_duplicates(seq):
    return len(seq) != len(set(seq))


if __name__ == '__main__':
	main()
