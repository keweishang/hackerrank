#!/bin/python

import sys


def bubblesort(numbers, length):
    switch_count = 0
    last_idx = 0
    for _ in range(0, 2):
        # Only need to iterate two times because each person can bribe maximum two times
        start_idx = length - 1
        # Starting from the minimum label at the end of the linebecause the 1st person
        # could be bribed all the time, which make him the last person in the line
        while last_idx < start_idx:
            if numbers[start_idx] < numbers[start_idx - 1]:
                # Swap
                tmp = numbers[start_idx]
                numbers[start_idx] = numbers[start_idx - 1]
                numbers[start_idx - 1] = tmp
                switch_count += 1
            start_idx -= 1
        last_idx += 1
    return switch_count


T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int, raw_input().strip().split(' '))

    chaotic = False
    # Too chaotic case
    for idx, element in enumerate(q):
        if element - idx > 3:
            chaotic = True
            break

    if chaotic:
        print 'Too chaotic'
    else:
        bribe_count = bubblesort(q, n)
        print str(bribe_count)
