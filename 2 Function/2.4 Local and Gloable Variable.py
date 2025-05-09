
# # A local variable is a variable declared inside a function.

# def f():
#     s = "I love Geeksforgeeks"   # local variable
#     print(s)

# f()  # calls the function


s = "I love gg" # 🔵 This is a global variable

def f():
    print("inside function",s)  # We can access x inside the function

f()
print("outside function",s)  # We can also access x outside the function
