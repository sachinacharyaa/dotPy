# Passing Function as an Argument
# In Python, we can pass functions as arguments to other functions. 
# We can pass a function by simply referencing its name without parentheses.


# Example:
# A function that takes another function as an argument

def fun(func, arg):          # 'func' is a function, 'arg' is a value
                             # It runs the function on the value
    return func(arg)


def square(x):               # A normal function that squares a number

    return x ** 2
# Calling fun and passing square function as an argument  

res = fun(square, 5)           # Call 'fun', pass 'square' and 5

print(res)