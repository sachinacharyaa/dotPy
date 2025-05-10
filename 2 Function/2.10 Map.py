# map() is a built-in function that lets you
# apply a function to every item in a list
# (or any iterable) — without writing a loop manually.


# Syntax of map
         
#       map(function, iterable)

#  function: the function you want to apply
 # iterable: a list, tuple, etc.



nums = [1, 2, 3, 4]

# Use map to square each number
squares = map(lambda x: x ** 2, nums)

print(list(squares))  
