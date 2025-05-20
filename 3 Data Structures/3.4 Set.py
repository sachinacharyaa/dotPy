# A set is a built-in data type in Python that:
 
# should be {}      set1 = {1 ,2 ,3}
#                   print(set1)

# Stores multiple items

# Does not allow duplicates

# Does not maintain order

# Is useful for things like: removing duplicates, checking membership, and doing set math (like union, intersection)

# Works with any iterable: strings, lists, tuples, dictionaries (keys only)


# Creating a Set empty
set1 = set()
print(set1)                       #set()

# Creating a Set with strings
set1 = set("GeeksForGeeks")
print(set1)                       #{' G', 'e ',' k' , 's ','F ','o', 'r'} 
                                  # or can comes in  random order 

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)                          # {'Geeks', 'For',}

# Creating a Set with the use of a tuple ( tuple ma set print garnu)
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# Creating a Set with the use of a dictionary ( dic ma pani set print garnu)
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))