"""input = 'abc decfghijakl'
answer = 'cfghijakl'

input = 'abcdaac'

dict [letter] = last position
range: min(beginning of non repeating character) to max
max_range, cur_range
if its in the dict: min = prev_last position and keep going
"""

def longestSubString(string):
    dict = {}
    min, min_r = None
    max_r = None
    range = None

    if len(string) == 0:
        return

    for let, i in enumerate(string):
        if let in string:
            if min is None:
                min = i
            if dict[let] > min:
                min = dict[let] + 1
        else:
            dict[let] = i

        if (i - min) > range or range is None:
            min_r = min
            max_r = i

    return string[min_r:max_r]
