#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findLongestSingleSlot' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts 2D_INTEGER_ARRAY leaveTimes as parameter.
#

def findLongestSingleSlot(leaveTimes):
    # Write your code here
    lenthLeaveTimes = len(leaveTimes)
    flagResult = 0
    flagMaxTime = 0
    timeLimit = []
    timeLimitNext = 0
    timeLimitFind = 0
    maxEle = 0
    # print(leaveTimes)
    for x in range(lenthLeaveTimes):
        flagResult = leaveTimes[x][0]
        timeLimitFind = (leaveTimes[x][1] - timeLimitNext)
        timeLimit.append(timeLimitFind)
        timeLimitNext = leaveTimes[x][1]
        maxEle = max(timeLimit)

    # print(maxEle)
    # print(timeLimit.index(maxEle))
    # print(leaveTimes[timeLimit.index(maxEle)][0])
    chars = 'abcdefghijklmnopqrstuvwxyz'
    # print(chars[leaveTimes[timeLimit.index(maxEle)][0]])

    return chars[leaveTimes[timeLimit.index(maxEle)][0]]


        # print(flagResult)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    leaveTimes_rows = int(input().strip())
    leaveTimes_columns = int(input().strip())

    leaveTimes = []

    for _ in range(leaveTimes_rows):
        leaveTimes.append(list(map(int, input().rstrip().split())))

    result = findLongestSingleSlot(leaveTimes)

    fptr.write(str(result) + '\n')

    fptr.close()

