# Operators are used to perform operations on values and variables. 
# In this article, we will look into different types of Python operators. 

# OPERATORS: These are the special symbols. Eg- + , * , /, etc.
# OPERAND: It is the value on which the operator is applied.


# 1. Arithmetic Operators
# Used to perform basic mathematical operations like addition, subtraction, multiplication and division.

# Variables
# a = 15
# b = 4

# # Addition
# print("Addition:", a + b)  

# # Subtraction
# print("Subtraction:", a - b) 

# # Multiplication
# print("Multiplication:", a * b)  

# # Division
# print("Division:", a / b) 

# # Floor Division - without decimal point
# print("Floor Division:", a // b)  

# # Modulus
# print("Modulus:", a % b) 

# # Exponentiation
# print("Exponentiation:", a ** b)





# 2> Comparison Operators
#  Relational operators are used to  compares the values.
# It either returns True or False according to the condition.

# a = 13
# b = 33

# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)





# 3> Logical operators perform Logical AND, Logical OR and Logical NOT operations. 
#    It is used to combine conditional statements.

# a = True
# b = False


# print(a and b)  #both should be same, then only it will return True
# print(a or b)   # Atleast one should be same, then only it will return True
# print(not a)   # It will return opposite of the value.




# 4> Assignment Operators
# Python Assignment operators are used to assign values to the variables.
# This operator is used to assign the value of the right side of the expression to the left side operand.

# Example of Assignment Operators in Python:

a = 10
b = 5


b += a     # b = b + a
print(b)

b -= a     # b = b - a
print(b)

b *= a     # b = b * a
print(b)

b <<= a    # b = b < a
print(b)
