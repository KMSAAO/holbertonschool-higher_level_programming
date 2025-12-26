#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "Javascript" }
set_2 = { "Python", "Javascript" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))