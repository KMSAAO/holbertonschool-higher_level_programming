#!/usr/bin/python3
def fizzbuzz():
    three = 3
    five = 5
    for i in range(1, 101): 
        if i % three and five == 0:
            print("FizzBuzz", end=" ")
            three *= 2
            five *= 2
        elif i == three:
            print("Fizz", end=" ")
            three = 2 * three
            continue
        elif i == five:
            print("Buzz", end=" ")
            five = 2 * five
            continue
        else:
            print("{}".format(i), end=" ")
            
        
        
