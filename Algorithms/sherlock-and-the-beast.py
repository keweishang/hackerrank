#!/bin/python

import sys

def findDecentNumber(n, counter):
    if n < 0:
        return False
    if n % 3 == 0:
        counter[3] = n/3
        return True
    elif findDecentNumber(n-5, counter):
        counter[5] += 1
        return True
    else:
        return False

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    counter = {3:0, 5:0}
    if findDecentNumber(n, counter):
        result = []
        for _ in range(counter[3]):
            result.extend(['5']*3)
        for _ in range(counter[5]):
            result.extend(['3'] * 5)
        print ''.join(result)
    else:
        print '-1'
