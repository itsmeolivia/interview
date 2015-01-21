
def duplicate(arr):
    if len(arr) < 2:
        return -1
    elif len(arr) == 2:
        return arr[0]
    else:
        arr.sort()
        prev = None
        for item in arr:
            if item == prev:
                return item
            prev = item

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
def shuffle(arr):
    random.shuffle(arr)
    return arr
