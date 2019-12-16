#!binpython3

import math
import os
import random
import re
import sys



# Complete the breakingRecords function below.
def breakingRecords(scores):

    highest = scores[0]
    lowest = scores[0]

    cnt_high = 0
    cnt_low = 0

    for i in range(len(scores)):
        if scores[i] > highest:
            highest = scores[i]
            cnt_high = cnt_high + 1
        if scores[i] < lowest:
            lowest = scores[i]
            cnt_low = cnt_low + 1
    
    scores = (cnt_high, cnt_low)
    return scores


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
    fptr.write(' '.join(map(str, result)))
    fptr.write(result+'\n')

    fptr.close()