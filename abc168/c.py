import os
import math

def main():
    a,b,h,m = map(int, input().split())

    rand2 = 6 * m
    rand3 = (0.5 * m) + (30 * h)
    rand_result = 0.0

    if (abs(rand3 - rand2) <= 180):
        rand_result = abs(rand3 - rand2)
    else:
        rand_result = 360 - abs(rand3 - rand2)

    
    ans = math.sqrt(pow(a,2) + pow(b,2) - (2*a*b*math.cos(math.radians(rand_result))))
    print(format(ans,'.10f'))

if __name__ == "__main__":
    main()