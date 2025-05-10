

# def fun(*args):       # accepts many positional
                        #  values like 1, 2, 3
#     return sum(args)

# print(fun(1, 2, 3, 4))      # Output: 10
# print(fun(5, 10, 15))       # Output: 30







# /////////////////// #  the difference is addtioal * and . values()//////////////////////////////////

def func(**kwargs):   # accepts many keyword arguments like name=John, age=25
    return sum(kwargs.values())

print(func( a =1 , b = 2, c = 4))

