#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    len0 = len(my_list)
    list0 = []
    for i in my_list:
        if i % 2 == 0:
            list0.append(True)
        else:
            list0.append(False)
    return (list0)
