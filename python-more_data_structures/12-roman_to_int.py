#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    result = 0
    rs = roman_string
    i = 0
    while i < len(rs):
        if rs[i] == "M":
            result += 1000
            i += 1
        elif i < len(rs) - 1 and rs[i] == "C" and rs[i + 1] == "M":
            result += 900
            i += 2
        elif i < len(rs) - 1 and rs[i] == "D" and rs[i + 1] == "C":
            result += 400
            i += 2
        elif rs[i] == "D":
            result += 500
            i += 1
        elif i < len(rs) - 1 and rs[i] == "X" and rs[i + 1] == "C":
            result += 90
            i += 2
        elif rs[i] == "C":
            result += 100
            i += 1
        elif rs[i] == "L":
            result += 50
            i += 1
        elif i < len(rs) - 1 and rs[i] == "X" and rs[i + 1] == "L":
            result += 40
            i += 2
        elif rs[i] == "X":
            result += 10
            i += 1
        elif i < len(rs) - 1 and rs[i] == "I" and rs[i + 1] == "X":
            result += 9
            i += 2
        elif i < len(rs) - 1 and rs[i] == "I" and rs[i + 1] == "V":
            result += 4
            i += 2
        elif rs[i] == "V":
            result += 5
            i += 1
        elif rs[i] == "I":
            result += 1
            i += 1
    return result
