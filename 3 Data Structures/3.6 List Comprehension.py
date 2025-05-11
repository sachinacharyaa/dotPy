# List comprehension is a way to create lists using a concise syntax.
# It allows us to generate a new list by applying an expression to each item in an
# existing iterable (such as a list or range). 


a = [ 1  , 4   , 8]

b = [ val ** 2 for val in a]
c = [ val ** 3 for val in a]

print(b)
print(c)









# Conditional statements in list comprehension
a = [1, 2, 3, 4, 5]

res = [val for val in a if val % 2 == 0]

print(res)




#Creating a list from a range# Creates a list of numbers from 0 to 9
a = [i for i in range(10)]

print(a)