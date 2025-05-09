# A return statement is used to end the execution of the function call and it “returns” 
# The statements after the return statements are not executed.


def add(a, b):

    # returning sum of a and b
    return a + b

def is_true(a):

    # returning boolean of a
    return bool(a)

# calling function
res = add(2, 3)
print(res)

res = is_true(2<5)
print(res)