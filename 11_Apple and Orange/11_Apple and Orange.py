import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    new_a = [i for i in apples if i+a >= s and i+a<=t]
    new_b = [i for i in oranges if i+b <= t and i+b>=s]
    print(len(new_a))
    print(len(new_b))

if __name__ == '__main__':
    st = input().split() # 집 [s,t]
    s = int(st[0]) 
    t = int(st[1])
    ab = input().split() # 사과나무, 오렌지나무 [a,b]
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split() # 개수
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
