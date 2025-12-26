#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

<<<<<<< HEAD
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
=======
tuple_a = (1,)
tuple_b = (1,)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, tuple_b))
>>>>>>> 748062073171fad7d23b39b9f1d5da4aff8ce5a9
