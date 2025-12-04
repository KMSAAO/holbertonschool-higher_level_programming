#!/usr/bin/python3
def no_c(my_string):
    new_string = "".join(filter(lambda x: x not in "cC", my_string))
    return (new_string)
