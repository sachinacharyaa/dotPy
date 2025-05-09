
# Data types are the classification or categorization of data items.

# Numeric – int, float, complex
# Sequence Type – string, list, tuple
# Mapping Type – dict
# Boolean – bool
# Set Type – set, frozenset
# Binary Types – bytes, bytearray, memoryview


# eg for  int, float, string, list and set

# x = 50    #int
# x = 60.5  #float
# x = "Hello World"  #string
# x = ["geeks", "for", "geeks"]
# x = ("geeks", "for", "geeks")



# 1. Numeric Data Types
# which represents the data that has a numeric value.
# It can be either an integer or a floating point number.
# Numeric – int, float, complex


# a = 5
# print(type(a))

# b = 5.0
# print(type(b))

# c = 2 + 4j
# print(type(c))





# 2.Sequence Data Types
# the ordered collection of similar or different Python data types.
# Sequence Type – string, list, tuple

# 2.1 String Data Type
# A string is a collection of characters enclosed in quotes.
# It can be either single quotes or double quotes.


# s = 'Welcome World'
# print(s)

# # check data type 
# print(type(s))

# # access string with index
# print(s[1])
# print(s[2])
# print(s[-1])



# 2.2 List Data Type []
# A list is a collection of items which can be of any data type including strings, integers,

# # Empty list
# a = []

# # list with int values
# a = [1, 2, 3]
# print(a)

# # list with mixed int and string
# b = ["Geeks", "For", "Geeks", 4, 5]
# print(b)


#2.3 Tuple Data Type ()
# Just like a list, a tuple is also an ordered collection of Python objects.

# initiate empty tuple
# tup1 = ()

# tup2 = ('Geeks', 'For')
# print("\nTuple with the use of String: ",
#     tup2)



# 3 Dictionary Data Type {}
#Dictionary is a data structure that stores the value in key: value pairs


# create dictionary using { }
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
#- only variable allowed inside(), not integer

d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)