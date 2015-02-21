def duplicate(arr):
    if len(arr) < 2:
        return -1
    else:
        arr.sort()
        prev = None
        for item in arr:
            if item == prev:
                return item
            prev = item
        return -1


def nonRepeat(line):
    if len(line) == 1:
        return line

    order = []
    count = {}

    for l in line:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
            order.append(l)
    for m in order:
        if count[m] == 1:
            return m
    return None

import random

def myshuffle(arr):
    random.shuffle(arr)
    return arr

def test():
    ansDuplicate = [-1, -1, -1, 3]
    dataDuplicate = [[], [1], [1, 2], [1, 2, 3, 3]]

    for i, j in zip(ansDuplicate, dataDuplicate):
        print duplicate(j) == i

    ansRepeat = ['\0', None, 'a', 'a', None, 'd']
    dataRepeat = ['\0','', 'a', 'abc', 'aabbcc', 'abcbcad']

    for i, j in zip(ansRepeat, dataRepeat):
        print nonRepeat(j) == i

test()
