# A recursive function is a function that calls itself to solve a smaller version of the same problem.



# Basic Structure of Recursive Function


# def recursive_function(parameters):
#     if base_case_condition:
#        return base_result


#     else:
#      return recursive_function(modified_parameters)


def factorial(n):
    if n == 0:
        return 1                                   #Base case: if n == 0: return 1 → stops the recursion,  last ma use vayo factorial(0) = 1
    else:
        return n * factorial(n-1)  
                                            # factorial(5) → 5 * factorial(4)

                                            # factorial(4) → 4 * factorial(3)

                                            # factorial(3) → 3 * factorial(2)

                                            # factorial(2) → 2 * factorial(1)

                                            # factorial(1) → 1 * factorial(0)
                                            
                                            #factorial(0) → 1 (this is the base case, it stops here)

print(factorial(5))