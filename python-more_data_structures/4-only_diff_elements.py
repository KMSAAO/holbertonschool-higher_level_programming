#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lis = list(set_1)
    lis.extend(set_2)
    for x in lis:
        if x in set_2 and x in set_1:
            lis.remove(x)
    return lis
